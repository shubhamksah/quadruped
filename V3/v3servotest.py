import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

angle = 90
angle2 = 135
angle3 = 45


kit.servo[1].angle = angle
kit.servo[2].angle = 125
kit.servo[3].angle = 85
kit.servo[4].angle = angle
kit.servo[5].angle = 40
kit.servo[6].angle = 90
kit.servo[7].angle = angle
kit.servo[8].angle = angle2
kit.servo[9].angle = 95
kit.servo[10].angle = angle
kit.servo[11].angle = angle3
kit.servo[12].angle = 95
