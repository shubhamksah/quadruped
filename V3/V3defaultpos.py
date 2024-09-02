import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

FLT = 88
FLF = 129
FLH = 100

FRT = 92
FRF = 43
FRH = 88

BLT = 100
BLF = 129
BLH = 95

BRT = 86
BRF = 51
BRH = 95 

try:

    kit.servo[2].angle = FLH
    kit.servo[5].angle = FRH
    kit.servo[8].angle = BLH
    kit.servo[11].angle = BRH 

    kit.servo[0].angle = 90
    # kit.servo[1].angle = FLF

    # kit.servo[3].angle = FRT
    # kit.servo[4].angle = FRF

    # kit.servo[6].angle = BLT
    # kit.servo[7].angle = BLF

    # kit.servo[9].angle = BRT
    # kit.servo[10].angle = BRF 

except:
    print("Exit")
    quit()