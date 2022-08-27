# Rubik

Code for solving the rubik cube using the robot
proposed in https://www.thingiverse.com/thing:3826740/comments


# set up

* pip install -r requirements.txt
* enable i2c
sudo raspi-config -> Interface options
* connect conector (5 pins to inner 5 first pins) (red, green, blue, none, black) -> (1)3v3 (3)gpio2 (5)gpio3 - (9) ground
* cammea connector, letter facing usb
* place cube so yellow faces camera and green is over the window with the cammara ribbon.
* RUN PROGRAM:   python ./main.py
