import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

angle = 90

kit.servo[1].angle = 91
kit.servo[2].angle = 90
kit.servo[3].angle = 84
# kit.servo[4].angle = 90
# kit.servo[5].angle = 90
# kit.servo[6].angle = 90 
# kit.servo[7].angle = angle 
# kit.servo[8].angle = angle 
# kit.servo[9].angle = 95
# kit.servo[10].angle = angle 
# kit.servo[11].angle = angle 
# kit.servo[12].angle = angle 