# import the necessary packages
from time import sleep
from servo import Servo
from camera import Camera
from calibrate import (fileNames)



class TakePictures():
    """ This class takes the six pictures needed to identy the color
        of each square in each face"""
    # F -> frint, L-> left, b -> back, r -> right
    faceOrder = ['F','L','B','R']
	
    def __init__(self):
       self.servo = Servo()
       sleep(3)
       self.servo.grip()
       self.camera = Camera()

    def adquire(self):
        # Take 6 pictures
        # one per face

        for key in self.faceOrder:
            print("taking image", fileNames[key], flush=True)
            self.camera.takePicture(fileNames[key])
            self.servo.rotNextHorizontal()
        self.servo.rotNextVertical()
        print("taking image", fileNames['U'], flush=True)
        self.camera.takePicture(fileNames['U'])
        self.servo.rotNextVertical()
        self.servo.rotNextVertical()
        print("taking image", fileNames['D'], flush=True)
        self.camera.takePicture(fileNames['D'])
        print("Placing Front facing camera", flush=True)
        self.servo.rotNextVertical()
        self.camera.stopPreview()

