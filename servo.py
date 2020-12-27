# rotate cube
import time
import Adafruit_PCA9685

LEFT_GRIPPER  = 5
LEFT_HOLDER   = 4
RIGHT_GRIPPER = 7
RIGHT_HOLDER  = 6
RELAX = 30
SLEEP = 0.001
STEP = 1  # 5 * 5 * 3 * 3
WAIT=0.5

class Servo():
    """ class to manage servo TowerPro MG995R"""
    # Set maximum and minimum values of the servos
    # sets min, max pwm frequency
    servo_min_max = {}
    servo_min_max[LEFT_HOLDER]  = (225,455) # gripper left
    servo_min_max[RIGHT_HOLDER] = (300,535) # gripper right
    servo_min_max[LEFT_GRIPPER]   = (175,310) # holder left
    servo_min_max[RIGHT_GRIPPER]  = (175,310) # holder right
    
    def __init__(self):
       # Initialise the PCA9685 using the default address (0x40).
       self.pwm = Adafruit_PCA9685.PCA9685()

       # Set frequency to 60hz, good for servos.
       self.pwm.set_pwm_freq(60)

       # create dictionary for min and max
       # this is not necessary but produce cleaner code
       self.min = {}
       self.max = {}
       for id, value in self.servo_min_max.items():
           self.min[id] = value[0]
           self.max[id] = value[1]

       # reset servo state
       self.openForCube()
   
    def rotate(self, id,  pulse):
        """Auxiliary function needed to adjust max min
           id: servo id
           pulse: frequency
        """ 
        self.pwm.set_pwm(id, 0, pulse)
 
    def openL(self):
        "fuly open left gripper "
        self.pwm.set_pwm(LEFT_GRIPPER, 0, self.max[LEFT_GRIPPER])

    def openR(self):
        "fuly open right gripper "
        self.pwm.set_pwm(RIGHT_GRIPPER, 0, self.max[RIGHT_GRIPPER])

    def closeL(self):
        "close left gripper "
        self.pwm.set_pwm(LEFT_GRIPPER, 0, self.min[LEFT_GRIPPER])

    def closeR(self):
        "close open right gripper "
        self.pwm.set_pwm(RIGHT_GRIPPER, 0, self.min[RIGHT_GRIPPER])

    def relax(self):
        """open and close slightly servo grippers so cube may 
           adjust to initial position. Only relax if 
           holders are in initial state"""
        self.openForCube()
        time.sleep(.2)
        self.grip()

    def openForCube(self):
        """ Relax grip and align holders 
            so we may place the cube"""
        self.pwm.set_pwm(LEFT_GRIPPER, 0, 
                         self.min[LEFT_GRIPPER] + RELAX)
        self.pwm.set_pwm(RIGHT_GRIPPER, 0,
                         self.min[RIGHT_GRIPPER] + RELAX)
        self.pwm.set_pwm(RIGHT_HOLDER, 0, 
                         self.min[RIGHT_HOLDER])
        self.pwm.set_pwm(LEFT_HOLDER, 0,
                         self.min[LEFT_HOLDER])

    def grip(self):
        """ Grip cube"""
        self.pwm.set_pwm(LEFT_GRIPPER, 0, 
                         self.min[LEFT_GRIPPER])
        self.pwm.set_pwm(RIGHT_GRIPPER, 0,
                         self.min[RIGHT_GRIPPER])

    def clockwiseL(self, interval=0):
        """ rotate servo clockwise"""
        if interval !=0:
           self.pwm.set_pwm(LEFT_HOLDER, 0, self.max[LEFT_HOLDER])
        else:
           for pulse in range(self.min[LEFT_HOLDER],
                              self.max[LEFT_HOLDER], STEP):
               self.pwm.set_pwm(LEFT_HOLDER, 0, pulse)
               time.sleep(SLEEP)
    
    def clockwiseR(self, interval=0):
        """ rotate servo clockwise"""
        if interval !=0:
           self.pwm.set_pwm(RIGHT_HOLDER, 0, self.max[RIGHT_HOLDER])
        else:
           for pulse in range(self.min[RIGHT_HOLDER],
                              self.max[RIGHT_HOLDER], STEP):
               self.pwm.set_pwm(RIGHT_HOLDER, 0, pulse)
               time.sleep(SLEEP)
    
    def counterClockwiseL(self, interval=0):
        """ rotate left servo counterclockwise"""
        if interval !=0:
           self.pwm.set_pwm(LEFT_HOLDER, 0, self.min[LEFT_HOLDER])
        else:
           for pulse in range(self.max[LEFT_HOLDER],        
                              self.min[LEFT_HOLDER], -STEP):
               self.pwm.set_pwm(LEFT_HOLDER, 0, pulse)
               time.sleep(SLEEP)

    
    def counterClockwiseR(self, interval=0):
        """ rotate right servo counter clockwise"""
        if interval !=0:
           self.pwm.set_pwm(RIGHT_HOLDER, 0, self.min[RIGHT_HOLDER])
        else:
           for pulse in range(self.max[RIGHT_HOLDER],
                              self.min[RIGHT_HOLDER], -STEP):
               self.pwm.set_pwm(RIGHT_HOLDER, 0, pulse)
               time.sleep(SLEEP)

    def rotNextHorizontal(self, interval=0, wait=WAIT):
        self.openL(); time.sleep(wait)
        self.clockwiseR(interval); time.sleep(wait)
        self.closeL(); time.sleep(wait)
        self.openR(); time.sleep(wait)
        self.counterClockwiseR(interval); time.sleep(wait)
        self.closeR(); time.sleep(wait)
        self.relax(); time.sleep(wait)

    def rotNextVertical(self, interval=0, wait=WAIT):
        self.openR(); time.sleep(wait)
        self.clockwiseL(interval); time.sleep(wait)
        self.closeR(); time.sleep(wait)
        self.openL(); time.sleep(wait)
        self.counterClockwiseL(interval); time.sleep(wait)
        self.clockwiseR(interval); time.sleep(wait)
        self.closeL(); time.sleep(wait)
        self.openR(); time.sleep(wait)
        self.counterClockwiseR(interval); time.sleep(wait)
        self.clockwiseL(interval); time.sleep(wait)
        self.closeR(); time.sleep(wait)
        self.openL(); time.sleep(wait)
        self.counterClockwiseL(interval); time.sleep(wait)
        self.closeL(); time.sleep(wait)
        self.relax(); time.sleep(wait)

        for i in range(2):
            self.openR(); time.sleep(wait)
            self.clockwiseL(interval); time.sleep(wait)
            self.closeR(); time.sleep(wait)
            self.openL(); time.sleep(wait)
            self.counterClockwiseL(interval); time.sleep(wait)
            self.closeL(); time.sleep(wait)
            self.relax(); time.sleep(wait)

    def rotDown(self, interval=0, wait=WAIT, rounds=1):
        """Rotate down face clockwise 90 degrees and go back
           to standard possition"""
        for i in range(rounds):
            self.clockwiseR(interval); time.sleep(wait)
            self.openR(); time.sleep(wait)
            self.counterClockwiseR(interval=1); time.sleep(wait)
            self.closeR(); time.sleep(wait)
            self.relax(); time.sleep(wait)

    def rotBack(self, interval=0, wait=WAIT, rounds=1):
        """Rotate back face clockwise 90 degrees and go back
           to standard possition"""
        for i in range(rounds):
            self.clockwiseL(interval); time.sleep(wait)
            self.openL(); time.sleep(wait)
            self.counterClockwiseL(interval=1); time.sleep(wait)
            self.grip(); time.sleep(wait)
            self.relax(); time.sleep(wait)


    def rotLeft(self, interval=0, wait=WAIT, rounds=1):
        """Rotate left face clockwise 90 degrees and go back
           to standard possition"""
        self.openR(); time.sleep(wait)
        self.clockwiseL(interval); time.sleep(wait)
        self.closeR(); time.sleep(wait)
        self.openL(); time.sleep(wait)
        self.counterClockwiseL(1); time.sleep(wait)
        self.closeL(); time.sleep(wait)
        for i in range(rounds):
            self.relax();  time.sleep(wait)
            self.clockwiseR(); time.sleep(wait)
            self.openR(); time.sleep(wait)
            self.counterClockwiseR(1); time.sleep(wait)
            if i != (rounds -1):
                self.closeR(); time.sleep(wait) 

        ##self.openR(); time.sleep(wait)
        for i in range(3):
            self.clockwiseL(); time.sleep(wait)
            self.closeR(); time.sleep(wait)
            self.openL(); time.sleep(wait)
            self.counterClockwiseL(1); time.sleep(wait)
            self.closeL(); time.sleep(wait)
            self.relax(); time.sleep(wait)
            if i!=2:
                self.openR(); time.sleep(wait)

    def rotRight(self, interval=0, wait=WAIT, rounds=1):
        """Rotate left face clockwise 90 degrees and go back
           to standard possition"""
        self.openL(); time.sleep(wait)
        self.clockwiseR(interval); time.sleep(wait)
        self.closeL(); time.sleep(wait)
        self.openR(); time.sleep(wait)
        self.counterClockwiseR(1); time.sleep(wait)
        self.closeR(); time.sleep(wait)

        for i in range(rounds):
            self.relax();  time.sleep(wait)
            self.clockwiseL(); time.sleep(wait)
            self.openL(); time.sleep(wait)
            self.counterClockwiseL(1); time.sleep(wait)
            if i != (rounds -1):
                self.closeL(); time.sleep(wait)

        for i in range(3):
            self.clockwiseR(); time.sleep(wait)
            self.closeL(); time.sleep(wait)
            self.openR(); time.sleep(wait)
            self.counterClockwiseR(1); time.sleep(wait)
            self.closeR(); time.sleep(wait)
            self.relax(); time.sleep(wait)
            if i!=2:
                self.openL(); time.sleep(wait)

    def rotUp(self, wait=WAIT, rounds=1):
        for i in range(2):
            self.openR(); time.sleep(wait)
            self.clockwiseL(); time.sleep(wait)
            self.closeR(); time.sleep(wait)
            self.openL(); time.sleep(wait)
            self.counterClockwiseL(1); time.sleep(wait)
            self.closeL(); time.sleep(wait)
            
        for i in range(rounds):
            self.relax(); time.sleep(wait)
            self.clockwiseR(); time.sleep(wait)
            self.openR(); time.sleep(wait)
            self.counterClockwiseR(1); time.sleep(wait)
            if i != (rounds -1):
                 self.closeR(); time.sleep(wait)

        for i in range(2):
            self.openR(); time.sleep(wait)
            self.clockwiseL(); time.sleep(wait)
            self.closeR(); time.sleep(wait)
            self.openL(); time.sleep(wait)
            self.counterClockwiseL(1); time.sleep(wait)
            self.closeL(); time.sleep(wait)
            self.relax(); time.sleep(wait)
        
    def rotFront(self, wait=WAIT, rounds=1):
        for i in range(2):
            self.openL(); time.sleep(wait)
            self.clockwiseR(); time.sleep(wait)
            self.closeL(); time.sleep(wait)
            self.openR(); time.sleep(wait)
            self.counterClockwiseR(1); time.sleep(wait)
            self.closeR(); time.sleep(wait)

        for i in range(rounds):
            self.relax(); time.sleep(wait)
            self.clockwiseL(); time.sleep(wait)
            self.openL(); time.sleep(wait)
            self.counterClockwiseL(1); time.sleep(wait)
            if i != (rounds -1):
                 self.closeL(); time.sleep(wait)

        for i in range(2):
            self.openL(); time.sleep(wait)
            self.clockwiseR(); time.sleep(wait)
            self.closeL(); time.sleep(wait)
            self.openR(); time.sleep(wait)
            self.counterClockwiseR(1); time.sleep(wait)
            self.closeR(); time.sleep(wait)
            self.relax(); time.sleep(wait)
        

"""
w w r
r w b
o y y
"""



