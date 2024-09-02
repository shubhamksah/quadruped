import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

FLH = 100
FRH = 88
BLH = 95
BRH = 95 

FLT = 83
FLF = 139

FRT = 92
FRF = 44

BLT = 88
BLF = 137

BRT = 90
BRF = 49

try:

    kit.servo[2].angle = FLH
    kit.servo[5].angle = FRH
    kit.servo[8].angle = BLH
    kit.servo[11].angle = BRH 

    kit.servo[0].angle = 84
    kit.servo[1].angle = 139

    kit.servo[3].angle = 92
    kit.servo[4].angle = 44

    kit.servo[6].angle = 90
    kit.servo[7].angle = 137

    kit.servo[9].angle = 88
    kit.servo[10].angle = 49

except:
    print("Exit")
    quit()