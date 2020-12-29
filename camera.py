import time
from picamera import PiCamera

WIDTH = 1024
HEIGHT = 1024


class Camera():
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (WIDTH, HEIGHT)
        # self.camera.exposure_mode = 'auto'
        self.camera.iso = 800
        time.sleep(2)
        self.camera.shutter_speed = self.camera.exposure_speed
        self.camera.exposure_mode = 'off'
        g = self.camera.awb_gains
        self.camera.awb_mode = 'off'
        self.camera.awb_gains = g
        self.camera.start_preview()
        time.sleep(2)  # Camera warm-up time

    def takePicture(self, filename='dummy'):
         filename =  filename + ".jpg"
         my_file = open(filename, 'wb')
         self.camera.capture(my_file)
         my_file.close()

    def stopPreview(self):
        self.camera.stop_preview() 
