import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

FLH = 100
FRH = 88
BLH = 95
BRH = 95 

FLT = 84
FLF = 139

FRT = 94
FRF = 44

BLT = 90
BLF = 137 - 5

BRT = 89
BRF = 49 + 3

try:

    kit.servo[2].angle = FLH
    kit.servo[5].angle = FRH
    kit.servo[8].angle = BLH
    kit.servo[11].angle = BRH 

    kit.servo[0].angle = FLT
    kit.servo[1].angle = FLF

    kit.servo[3].angle = FRT
    kit.servo[4].angle = FRF

    kit.servo[6].angle = BLT
    kit.servo[7].angle = BLF

    kit.servo[9].angle = BRT
    kit.servo[10].angle = BRF

except:
    print("Exit")
    quit()