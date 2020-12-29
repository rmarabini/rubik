import time
from  servo import *
"""Testing the servos"""

servo = Servo()

#servo.openForCube()
print("press any key to continue")
time.sleep(2)
###nombre = input()
servo.grip()
##exit(0)
time.sleep(1)
servo.relax()


for i in range(5):
    servo.clockwiseR()
    time.sleep(0.5)
    servo.openR()
    time.sleep(0.5)
    servo.counterClockwiseR()
    time.sleep(0.5)
    servo.grip()
    time.sleep(0.5)
    servo.relax()
    time.sleep(0.5)
    servo.clockwiseL()
    time.sleep(0.5)
    servo.openL()
    time.sleep(0.5)
    servo.counterClockwiseL()
    time.sleep(0.5)
    servo.grip()
    time.sleep(0.5)
    servo.relax()
    time.sleep(0.5)



print("RIGHT holder")
for i in range(5):
    servo.clockwiseR()
    time.sleep(0.5)
    servo.openR()
    time.sleep(0.5)
    servo.counterClockwiseR()
    time.sleep(0.5)
    servo.grip()
    time.sleep(0.5)
    servo.relax()
    time.sleep(0.5)

#servo.initialState()

print("LEFT holder")
for i in range(5):
    servo.clockwiseL()
    time.sleep(0.5)
    servo.openL()
    time.sleep(0.5)
    servo.counterClockwiseL()
    time.sleep(0.5)
    servo.grip()
    time.sleep(0.5)
    servo.relax()
    time.sleep(0.5)

print("GREEPER")
for i in range(5):
    servo.clockwiseL()
    time.sleep(1)
    servo.counterClockwiseL()
    servo.relax()
    time.sleep(1)
    servo.clockwiseR()
    time.sleep(1)
    servo.counterClockwiseR()
    servo.relax()
    time.sleep(1)

time.sleep(2)
servo.initialState()
del servo

