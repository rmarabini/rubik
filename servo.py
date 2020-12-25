# rotate cube
import time
import Adafruit_PCA9685

LEFT_GRIPPER  = 5
LEFT_HOLDER   = 4
RIGHT_GRIPPER = 7
RIGHT_HOLDER  = 6
RELAX = 30
LEFT = 0
RIGHT = 1
STEP = 10

class servo():
    # Set maximum and minimum values of the servos
    servo_min_max = {}
    servo_min_max[LEFT_HOLDER]  = (230,455) # gripper left
    servo_min_max[LEFT_GRIPPER]   = (185,300) # holder left
    servo_min_max[RIGHT_HOLDER] = (305,535) # gripper right
    servo_min_max[RIGHT_GRIPPER]  = (185,300) # holder right
    
    def __init__(self, servo_id):
       # Initialise the PCA9685 using the default address (0x40).
       self.pwm = Adafruit_PCA9685.PCA9685()

       # Set frequency to 60hz, good for servos.
       self.pwm.set_pwm_freq(60)
       self.servo_id = servo_id
       # value_when_true if condition else value_when_false
       if servo_id==LEFT_GRIPPER:
           self.servo_pair_id = RIGHT_GRIPPER
       elif servo_id==RIGHT_GRIPPER:
           self.servo_pair_id = LEFT_GRIPPER
       elif servo_id==LEFT_HOLDER:
           self.servo_pair_id = RIGHT_HOLDER
       elif servo_id==RIGHT_HOLDER:
           self.servo_pair_id = LEFT_HOLDER
       else:
           print("Unknown serve,  No respiro bye")
           exit(0)
       self.min = {}
       self.max = {}
       self.min[servo_id] = self.servo_min_max[servo_id][0]
       self.max[servo_id] = self.servo_min_max[servo_id][1]
       self.min[self.servo_pair_id] =
            self.servo_min_max[self.servo_pair_id][0]
       self.max[self.servo_pair_id] =
            self.servo_min_max[self.servo_pair_id][1]
   
    def rotate(self, id,  pulse):
        self.pwm.set_pwm(id, 0, pulse)

    def open(self, id=RIGHT):
        print("open")
        self.clockwise(id)

    def clockwise(self, id):
        """ rotate servo clockwise"""
        # channel: The channel that should be updated with the new values (0..15)
        # on: The tick (between 0..4095) when the signal should transition from low to high
        # off:the tick (between 0..4095) when the signal should transition from high to low
        self.pwm.set_pwm(id, 0, self.max)
    
    def close(self, id=RIGHT):
        print("close")
        self.counterclockwise(id)

    def counterclockwise(self, id):
        """ rotate servo counter clockwise"""
        self.pwm.set_pwm(id, 0, self.min[id])

    def relax(self):
        # open and close elightly servos so cube may 
        # adjust o initial position
        # open slightly both servos
        print("relax")
        self.pwm.set_pwm(self.servo_id, 0, 
                         self.min[self.servo_id] + RELAX)
        self.pwm.set_pwm(self.servo_pair_id, 0,
                         self.min[self.servo_pair_id] + RELAX)
        time.sleep(.2)
        self.pwm.set_pwm(self.servo_id, 0, 
                         self.min[self.servo_id])
        self.pwm.set_pwm(self.servo_pair_id, 0,
                         self.min[self.servo_pair_id])

    def placeCube(self):
       print("placeCube")
       self.end()

    def reset(self):
        self.grip()

    def grip(self):
       print("grip")
       self.pwm.set_pwm(self.servo_id, 0, 
                        self.min[self.servo_id])         
       self.pwm.set_pwm(self.servo_pair_id, 0, 
                        self.min[self.servo_pair_id])

    def end(self):
       print("end")
       self.pwm.set_pwm(self.servo_id, 0, 
                        self.min[self.servo_id] + RELAX)         
       self.pwm.set_pwm(self.servo_pair_id, 0, 
                        self.min[self.servo_pair_id] + RELAX)

    def rotateClock(self, servo_id, interval=0):
         if interval !=0:
            self.pwm.set_pwm(servo_id, 0, self.max[servo_id])
         else:
            for pulse in range(self.min, self.max[servo_id], STEP):
                self.pwm.set_pwm(servo_id, 0, pulse)
                time.sleep(0.1)

    def rotateCounterClock(self, servo_id, interval=0):
         if interval !=0:
            self.pwm.set_pwm(servo_id, 0, self.min[servo_id])
         else:
            for pulse in range(self.max, self.min[servo_id], -STEP):
                self.pwm.set_pwm(servo_id, 0, pulse)
                time.sleep(0.1)

