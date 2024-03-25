import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

kit.servo[1].angle = 90 
kit.servo[2].angle = 135
time.sleep(1)