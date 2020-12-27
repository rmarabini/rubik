# import the necessary packages
import numpy as np
import argparse
import cv2
import collections
import os
from picamera import PiCamera
from time import sleep

WIDTH = 1024
HEIGHT = 1024

numPixels = WIDTH * HEIGHT
errorPercentage = 0.14
camera = PiCamera()
camera.resolution = (WIDTH, HEIGHT)
camera.exposure_mode = 'auto'



def checkFinishObject():
    try:
        camera.start_preview()
        sleep(1)
        camera.capture('./finishImages/finish.jpg')
        camera.stop_preview()

        # load the image
        image = cv2.imread("./finishImages/finish.jpg")
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


        boundariesHSV = [
            ([0, 65, 65], [5, 255, 255]),  # red
            ([300, 65, 65], [1000, 255, 255]),  # red
            #([88, 183, 45], [100, 255, 255]),  # blue
            #([12, 194, 132], [23, 255, 255]),  # yellow
            #([36, 133, 106], [48, 255, 255]),  # green
            #([36, 133, 106], [48, 255, 255]),  # white
            ([10, 65, 65], [20, 255, 255])  # orange
        ]

        finalMask = np.zeros((HEIGHT, WIDTH), dtype="uint8")

        for index, (lower, upper) in enumerate(boundariesHSV):
            # create NumPy arrays from the boundaries
            lower = np.array(lower, dtype="uint8")
            upper = np.array(upper, dtype="uint8")

            # find the colors within the specified boundaries and apply
            # the mask

            mask = cv2.inRange(image_hsv, lower, upper)

            if index == 0:
                correct_pixels = np.count_nonzero(mask == 255)
                print("Pixeli rosi", correct_pixels)
                if correct_pixels > errorPercentage * numPixels:
                    return "red"

            elif index == 1:
                correct_pixels = np.count_nonzero(mask == 255)
                print("Pixeli albastri", correct_pixels)
                if correct_pixels > errorPercentage * numPixels:
                    return "blue"

            elif index == 2:
                correct_pixels = np.count_nonzero(mask == 255)
                print("Pixeli galbeni", correct_pixels)
                if correct_pixels > errorPercentage * numPixels:
                    return "yellow"

            elif index == 3:
                correct_pixels = np.count_nonzero(mask == 255)
                print("Pixeli verzi", correct_pixels)
                if correct_pixels > errorPercentage * numPixels:
                    return "green"

            cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('mask', 600, 600)
            print("finalMask, mask", finalMask.shape, mask.shape)
            finalMask = cv2.bitwise_or(finalMask, mask)
            cv2.imshow('mask', finalMask)
        output = cv2.bitwise_and(image_hsv, image_hsv, mask=finalMask)
        cv2.namedWindow('images', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('images', 600, 600)
        cv2.imshow("images", np.hstack([cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR), cv2.cvtColor(output, cv2.COLOR_HSV2BGR)]))
        cv2.waitKey(0)
        return "none"
    except KeyboardInterrupt:
        print("Interrupt")
    #finally:
        #if os.path.exists("./finishImages/finish.jpg"):
            #os.remove("./finishImages/finish.jpg")
       # else:
            #print("The file does not exist")





if __name__=="__main__":
    for i in range(0,1):
        #print("Making picture for test : " + str(i))
        result = checkFinishObject()
        print("Conclusion after the picture : " + str(i) + "is : " + result)

