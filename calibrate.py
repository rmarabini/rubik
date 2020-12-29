from PIL import Image
from itertools import chain
DEBUG=True
fileNames={'F':'front', 
           'L':'left', 
           'B':'back', 
           'R':'right', 
           'U':'up', 
           'D':'down'}

class GetInitialPosition():
    """ get color of each square in each face """
    def __init__(self):
        # center of each square
        inc = 250
        top_row_pxl = 200  #values for cube detection
        mid_row_pxl = top_row_pxl + inc
        bot_row_pxl = mid_row_pxl + inc
        lft_col_pxl = 280
        mid_col_pxl = lft_col_pxl + inc
        rgt_col_pxl = mid_col_pxl + inc
        self.pxl_locs =\
            [[(lft_col_pxl, top_row_pxl),(mid_col_pxl, top_row_pxl),(rgt_col_pxl, top_row_pxl)],
             [(lft_col_pxl, mid_row_pxl),(mid_col_pxl, mid_row_pxl),(rgt_col_pxl, mid_row_pxl)],
             [(lft_col_pxl, bot_row_pxl),(mid_col_pxl, bot_row_pxl),(rgt_col_pxl, bot_row_pxl)]
            ]
        self.wb_row_pxl = 950 #area for white balance
        self.wb_col_pxl = 950
	
        self.referenceColors={}
        self.referenceWhites={}
        
	# access order set by kociemba module
        self.kociembaOrder = ['U','R','F','D','L','B']
        self.col_sticker = []  # list with sticker colors


    def scanFiles(self):

        def pix_average(im, x,y):
	    """ compute pixel average around square center"""
            r,g,b = 0,0,0
            for i in range (0,10):
                for j in range (0,10):
                   r1,g1,b1 = im.getpixel((x-5+i,y-5+j))
                   r += r1
                   g += g1
                   b += b1
            r = r/100.
            g = g/100.
            b = b/100.
            return [r, g, b]

        def euclidean(a,b):
	    """ euclidean distance"""
            return (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2

        # for each image find reference colors (the central square color)
        for k, v in fileNames.items():  # for each image
            im = Image.open(v + ".jpg")
            im = im.convert('RGB')
	    # for each image store the central square color
            self.referenceColors[k] = \
                  pix_average(im,self.pxl_locs[1][1][0],
                                  self.pxl_locs[1][1][1]) # middle
	    # for each image store the value of a white area
            self.referenceWhites[k] = \
                  pix_average(im,
                             self.wb_col_pxl,
                             self.wb_row_pxl) # white balance
 
        # renormalize brightness
        maxWhite = [0,0,0]
        m = maxWhite
        for w in self.referenceWhites.values():
            if (w[0]**2 + w[1]**2 + w[2]**2) > \
               (m[0]**2 + m[1]**2 + m[2]**2):
                maxWhite = w

        for k in self.referenceColors.keys():
           for i in range(3):
              self.referenceWhites[k][i] /= maxWhite[i]
              self.referenceColors[k][i] /= self.referenceWhites[k][i]

        pxl_locs_list = []
        for i in range(3):
            for j in range(3):
                pxl_locs_list.append(self.pxl_locs[i][j])

        # self.kociembaOrder = ['U','R','F','D','L','B']
        for imageKey in self.kociembaOrder:  # for each image
            imageName = fileNames[imageKey] + ".jpg"
            for loc in pxl_locs_list:  # for each square
                im = Image.open(imageName)
                im = im.convert('RGB')
                average = pix_average(im, loc[0], loc[1]) # get averaged pixel value
            
                # find euclidian distances
                averaged_pixel = []
                for i in range(3):
                   averaged_pixel.append( average[i] / self.referenceWhites[imageKey][i])

                minDistance = 255 * 255
                winner = ""
                for kc, referenceColor in self.referenceColors.items():
                    distance = euclidean(referenceColor, averaged_pixel)
                    if distance < minDistance:
                        minDistance = distance
                        winner = kc
                self.col_sticker.append(winner)
                #print("self.col_sticker", len(self.col_sticker), self.col_sticker)

    def printCube(self, mapper=None):
        """ print cube using the mmaper to  map posions to colors"""
        counter = 0
        validateDict={'U':0,'R':0,'F':0,'D':0,'L':0,'B':0}
        for k in self.kociembaOrder:
            print("")
            print(fileNames[k] + ":")
            for x_iter in range(0,3): 
                for y_iter in range(0,3):
                    validateDict[self.col_sticker[counter]] += 1
                    if mapper is None:
                        print(self.col_sticker[counter], end = " ")
                    else:
                        print(mapper[self.col_sticker[counter]],
                              end = " ")
                    counter += 1
                print("")
        print("validateDict", validateDict) 

    def getCubeString(self):
        return ''.join(self.col_sticker)
