import time
from  camera import *
from servo import *

camera = Camera()
servo = Servo()
time.sleep(2.)
fileNames=['front', 'left', 'back', 'right', 'top', 'botton']

servo.grip()
time.sleep(0.5)

for counter in range(4):
    camera.takePicture(fileNames[counter])
    servo.rotNextHorizontal()
servo.rotNextVertical()
counter = 4
camera.takePicture(fileNames[counter])
servo.rotNextVertical()
servo.rotNextVertical()
counter = 5
camera.takePicture(fileNames[counter])
servo.rotNextVertical()

camera.stopPreview()
servo.openForCube()

