import time
import pygame
from adafruit_servokit import ServoKit

#Default Standing

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

#Variables

FLT1 = 88 + 65
FLF1 = 129 + 30

FRT1 = 92 - 65
FRF1 = 43 - 30

BLT1 = 100 + 65
BLF1 = 129 + 30

BRT1 = 86 - 65
BRF1 = 51 - 30

Pos2T = 65 #Tibia Movement in Position 2
Pos2F = 30 #Femur Movement in Position 2

Pos2TIncrement = Pos2T/160 #Tibia Movement Increment Position 2
Pos2FIncrement = Pos2F/160 #Femur Movement Increment Position 2

Pos2delay = 0.0000000001 #Position 2 Speed (Lower = Faster)
Pos3delay = 0.0000000001 #Position 3 Speed (Lower = Faster)

MovementDelay = 0.0 #Full Movement Speed (Lower = Faster)

kit = ServoKit(channels=16) #Initializes Servos

def main():

    t = 0

    pos1move = Pos2FIncrement
    pos2move = Pos2TIncrement

    while pos2move <= Pos2T: 
        kit.servo[1].angle = FLF + pos1move
        kit.servo[4].angle = FRF - pos1move
        kit.servo[7].angle = BLF + pos1move
        kit.servo[10].angle = BRF - pos1move
        pos1move += Pos2FIncrement
        kit.servo[0].angle = FLT + pos2move
        kit.servo[3].angle = FRT - pos2move
        kit.servo[6].angle = BLT + pos2move
        kit.servo[9].angle = BRT - pos2move
        pos2move += Pos2TIncrement
        kit.servo[2].angle = FLH
        kit.servo[5].angle = FRH
        kit.servo[8].angle = BLH
        kit.servo[11].angle = BRH  
        time.sleep(Pos2delay)

    time.sleep(1)

    pos1move = Pos2FIncrement
    pos2move = Pos2TIncrement

    while pos2move <= Pos2T: 
        kit.servo[1].angle = FLF1 - pos1move
        kit.servo[4].angle = FRF1 + pos1move
        kit.servo[7].angle = BLF1 - pos1move
        kit.servo[10].angle = BRF1 + pos1move
        pos1move += Pos2FIncrement
        kit.servo[0].angle = FLT1 - pos2move
        kit.servo[3].angle = FRT1 + pos2move
        kit.servo[6].angle = BLT1 - pos2move
        kit.servo[9].angle = BRT1 + pos2move
        pos2move += Pos2TIncrement
        kit.servo[2].angle = FLH
        kit.servo[5].angle = FRH
        kit.servo[8].angle = BLH
        kit.servo[11].angle = BRH  
        time.sleep(Pos2delay)

    # kit.servo[2].angle = FLH
    # kit.servo[5].angle = FRH
    # kit.servo[8].angle = BLH
    # kit.servo[11].angle = BRH 

    # kit.servo[0].angle = FLT
    # kit.servo[1].angle = FLF

    # kit.servo[3].angle = FRT
    # kit.servo[4].angle = FRF

    # kit.servo[6].angle = BLT
    # kit.servo[7].angle = BLF

    # kit.servo[9].angle = BRT
    # kit.servo[10].angle = BRF

if __name__ == "__main__":
    main()