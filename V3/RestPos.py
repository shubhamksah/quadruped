import time
import pygame
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

rest=90

#Default Positions
FLH = 100
FRH = 88
BLH = 95
BRH = 95 
FLT = rest
FLF = 95
FRT = rest
FRF = rest
BLT = rest
BLF = 85
BRT = rest
BRF = rest

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