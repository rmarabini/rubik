from kociemba import solve

class Solver():
    """ interface  with the kociemba module which has implemented the logic that
    solves the cube (see http://kociemba.org/cube.htm)"""

    def __init__(self, cubeString, servo):
        """cubeString: is a string that codifify the cube state
	   see http://kociemba.org/cube.htm for details
	   commandList: list of movements that will solve the cube
	   """
        self.commandList = solve(cubeString).split()
        self.mapper = {
                       "F" : servo.rotFront,
                       "L" : servo.rotLeft,
                       "R" : servo.rotRight,
                       "D" : servo.rotDown,
                       "U" : servo.rotUp,
                       "B" : servo.rotBack,
                      }

    def solveCube(self):
        """ maps the list of movements that will solve the cube -kociemba-
	as rotations that the rubik robot is able to perform.
	1 -> 90 degrees totation
	2-> 180 degree rotation
	3-> 270 degrees rotation or -90
	"""
	
        for command in self.commandList:
             if len(command)>1:
                if command[1] == "'": rounds = 3
                else: rounds = 2 
             else:
                rounds=1
             self.mapper[command[0]](wait=0.5, rounds=rounds)
