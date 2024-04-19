import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

angle = 90
angle2 = 135
angle3 = 45


kit.servo[1].angle = 60
kit.servo[2].angle = 125
kit.servo[3].angle = 85
kit.servo[4].angle = 120
kit.servo[5].angle = 50
kit.servo[6].angle = 90
kit.servo[7].angle = 60
kit.servo[8].angle = 135
kit.servo[9].angle = 95
kit.servo[10].angle = 120
kit.servo[11].angle = 40
kit.servo[12].angle = 95
