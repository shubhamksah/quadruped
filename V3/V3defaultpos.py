import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

FLH = 100
FRH = 88
BLH = 95
BRH = 95 

FLT = 88
FLF = 129

FRT = 92
FRF = 43

BLT = 100
BLF = 129

BRT = 86
BRF = 51

try:

    kit.servo[2].angle = FLH
    kit.servo[5].angle = FRH
    kit.servo[8].angle = BLH
    kit.servo[11].angle = BRH 

    kit.servo[0].angle = 83
    kit.servo[1].angle = 94 + 45

    kit.servo[3].angle = 90 + 2
    kit.servo[4].angle = 90 - 1 - 45

    kit.servo[6].angle = 90 - 2
    kit.servo[7].angle = 90 + 2 + 45

    kit.servo[9].angle = 90
    kit.servo[10].angle = 90 + 6

except:
    print("Exit")
    quit()