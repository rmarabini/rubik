import time
from picamera import PiCamera

IMG_BREITE = 64 
IMG_HOEHE = 64

top_row_pxl = 11  #values for cube detection
mid_row_pxl = 26
bot_row_pxl = 42
lft_col_pxl = 19
mid_col_pxl = 34
rgt_col_pxl = 50

wb_row_pxl = 60 #area for white balance
wb_col_pxl = 60

pxl_locs = [[(lft_col_pxl, top_row_pxl),(mid_col_pxl, top_row_pxl),(rgt_col_pxl, top_row_pxl)],
            [(lft_col_pxl, mid_row_pxl),(mid_col_pxl, mid_row_pxl),(rgt_col_pxl, mid_row_pxl)],
            [(lft_col_pxl, bot_row_pxl),(mid_col_pxl, bot_row_pxl),(rgt_col_pxl, bot_row_pxl)]]

class getFaceColors():

    def __init__(self):
        self.cubeString = ""
    
    def pixAverage(self, x, y):
        pass

    def readImage(self, counter):
        pass

    def getCubeString(self):
        return self.cubeString


class Camera():
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (IMG_BREITE, IMG_HOEHE)
        self.camera.exposure_mode = 'auto'
        self.camera.start_preview()
        time.sleep(2)  # Camera warm-up time

    def takePicture(self, filename='dummy'):
         filename =  filename + ".jpg"
         my_file = open(filename, 'wb')
         self.camera.capture(my_file)
         my_file.close()

    def stopPreview(self):
        self.samera.top_preview() 

    def analyzePicture(self):
        pass
