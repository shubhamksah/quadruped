import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

kit.servo[1].angle = 90 
time.sleep(1)