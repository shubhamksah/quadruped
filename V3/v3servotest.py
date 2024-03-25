import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

kit.servo[12].angle = 90 
kit.servo[9].angle = 90 
kit.servo[3].angle = 90 
kit.servo[6].angle = 120 