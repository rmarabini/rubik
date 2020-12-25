# rotate cube
import time
import Adafruit_PCA9685

LEFT_GRIPPER  = 5
LEFT_HOLDER   = 4
RIGHT_GRIPPER = 7
RIGHT_HOLDER  = 6
RELAX = 30

STEP = 10

class servo():
    """ class to manage servo TowerPro MG995R"""
    # Set maximum and minimum values of the servos
    # sets min, max pwm frequency
    servo_min_max = {}
    servo_min_max[LEFT_HOLDER]  = (230,455) # gripper left
    servo_min_max[RIGHT_HOLDER] = (305,535) # gripper right
    servo_min_max[LEFT_GRIPPER]   = (185,300) # holder left
    servo_min_max[RIGHT_GRIPPER]  = (185,300) # holder right
    
    def __init__(self, servo_id):
       # Initialise the PCA9685 using the default address (0x40).
       self.pwm = Adafruit_PCA9685.PCA9685()

       # Set frequency to 60hz, good for servos.
       self.pwm.set_pwm_freq(60)

       # create dictionary for min and max
       # this is not necessary but produce cleaner code
       self.min = {}
       self.max = {}
       for id, value in servo_min_max.items()
           self.min[id] = value[0]
           self.max[id] = value[1]
   
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

    def relax(self):
        """open and close slightly servo grippers so cube may 
           adjust to initial position"""
        self.placeCube()
        time.sleep(.2)
        self.grip()

    def placeCube(self):
       """ Relax grip so we may place the cube"""
        self.pwm.set_pwm(LEFT_GRIPPER, 0, 
                         self.min[LEFT_GRIPPER] + RELAX)
        self.pwm.set_pwm(RIGHT_GRIPPER, 0,
                         self.min[RIGHT_GRIPPER] + RELAX)

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
           for pulse in range(self.min[LEFT_HOLDER], self.max[LEFT_HOLDER], STEP):
               self.pwm.set_pwm(LEFT_HOLDER, 0, pulse)
               time.sleep(0.1)
    
    def clockwiseR(self, interval=0):
        """ rotate servo clockwise"""
        if interval !=0:
           self.pwm.set_pwm(RIGHT_HOLDER, 0, self.max[RIGHT_HOLDER])
        else:
           for pulse in range(self.min[RIGHT_HOLDER], self.max[RIGHT_HOLDER], STEP):
               self.pwm.set_pwm(RIGHT_HOLDER, 0, pulse)
               time.sleep(0.1)
    
    def counterClockwiseL(self, interval=0):
        """ rotate left servo counterclockwise"""
        if interval !=0:
           self.pwm.set_pwm(LEFT_HOLDER, 0, self.min[LEFT_HOLDER])
        else:
           for pulse in range(self.max[LEFT_HOLDER], self.min[LEFT_HOLDER], -STEP):
               self.pwm.set_pwm(LEFT_HOLDER, 0, pulse)
               time.sleep(0.1)
    
    def counterClockwiseR(self, interval=0):
        """ rotate right servo counter clockwise"""
        if interval !=0:
           self.pwm.set_pwm(RIGHT_HOLDER, 0, self.min[RIGHT_HOLDER])
        else:
           for pulse in range(self.max[RIGHT_HOLDER], self.min[RIGHT_HOLDER], -STEP):
               self.pwm.set_pwm(RIGHT_HOLDER, 0, pulse)
               time.sleep(0.1)
    
