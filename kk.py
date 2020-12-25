import time
from  rotador import *

servoGrip = servo(RIGHT_GRIPPER)
servoHold = servo(RIGHT_HOLDER)
# servoGrip.open(RIGHT_GRIPPER); servoGrip.open(LEFT_GRIPPER)
servoGrip.placeCube()
servoHold.reset()

print("press any key to continue")
nombre = input()
servoGrip.grip()

servoHold = servo(RIGHT_HOLDER)
servoHold.rotateClock(RIGHT_HOLDER,1)
servoHold.rotateCounterClock(RIGHT_HOLDER,1)



del servoGrip
del servoHold

