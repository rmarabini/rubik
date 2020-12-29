# Solce the Rubok cube, main routine
# import the necessary packages
from time import sleep
from servo import Servo
#from camera import Camera
from calibrate import (GetInitialPosition)
from takePictures import  TakePictures
from solver import Solver
# IMPORTANT place central white square 
# in from face

# adquire six faces picture
takePictures = TakePictures()
takePictures.adquire()

#relax servo
takePictures.servo.openForCube()

# get initial values for each square in each face
calibrate = GetInitialPosition()
calibrate.scanFiles()
mapper={'U':'R', 'R':'G', 'F':'W','D':'O','L':'B','B':'Y'}
print("place the cube so the middle square color is:")
print(mapper)
calibrate.printCube(mapper=mapper)
cubestring = calibrate.getCubeString(); print(cubestring)

# solve
solve = Solver(cubestring, takePictures.servo)
print('mapper', mapper)
print(solve.commandList)
takePictures.servo.grip()
sleep(0.5)
solve.solveCube()
takePictures.servo.openForCube()
