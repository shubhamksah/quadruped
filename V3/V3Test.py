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

FLT1 = 88 + 68
FLF1 = 129 + 30

FRT1 = 92 - 68
FRF1 = 43 - 30

BLT1 = 100 + 68
BLF1 = 129 + 30

BRT1 = 86 - 68
BRF1 = 51 - 30

#Variables

FLT2 = FLT1 - 48
FLF2 = FLF1 - 15

FRT2 = FRT1 + 48
FRF2 = FRF1 + 15

BLT2 = BLT1 - 48
BLF2 = BLF1 - 15

BRT2 = BRT1 + 48
BRF2 = BRF1 + 15

Pos1T = 20 #Tibia Movement in Position 1
Pos1F = 15 #Femur Movement in Position 1

Pos2T = 68 #Tibia Movement in Position 2
Pos2F = 30 #Femur Movement in Position 2

Pos3T = 48 #Tibia Movement in Position 3
Pos3F = 15 #Femur Movement in Position 3

Pos1TIncrement = Pos1T/40 #Tibia Movement Increment Position 2
Pos1FIncrement = Pos1F/40 #Femur Movement Increment Position 2

Pos2TIncrement = Pos2T/40 #Tibia Movement Increment Position 2
Pos2FIncrement = Pos2F/40 #Femur Movement Increment Position 2

Pos3TIncrement = Pos3T/40 #Tibia Movement Increment Position 2
Pos3FIncrement = Pos3F/40 #Femur Movement Increment Position 2

Posdelay = 0.000000000001 #Position 2 Speed (Lower = Faster)

MovementDelay = 0.0 #Full Movement Speed (Lower = Faster)

kit = ServoKit(channels=16) #Initializes Servos

def main():

    t = 0

    pos1move = Pos1FIncrement
    pos2move = Pos1TIncrement

    while pos2move <= Pos1T: 
        kit.servo[1].angle = FLF2 - pos1move
        kit.servo[4].angle = FRF2 + pos1move
        kit.servo[7].angle = BLF2 - pos1move
        kit.servo[10].angle = BRF2 + pos1move
        pos1move += Pos1FIncrement
        kit.servo[0].angle = FLT2 - pos2move
        kit.servo[3].angle = FRT2 + pos2move
        kit.servo[6].angle = BLT2 - pos2move
        kit.servo[9].angle = BRT2 + pos2move
        pos2move += Pos1TIncrement
        kit.servo[2].angle = FLH
        kit.servo[5].angle = FRH
        kit.servo[8].angle = BLH
        kit.servo[11].angle = BRH  
        time.sleep(Posdelay)

    time.sleep(1)

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
        time.sleep(Posdelay)

    time.sleep(1)

    pos1move = Pos3FIncrement
    pos2move = Pos3TIncrement

    while pos2move <= Pos3T: 
        kit.servo[1].angle = FLF1 - pos1move
        kit.servo[4].angle = FRF1 + pos1move
        kit.servo[7].angle = BLF1 - pos1move
        kit.servo[10].angle = BRF1 + pos1move
        pos1move += Pos3FIncrement
        kit.servo[0].angle = FLT1 - pos2move
        kit.servo[3].angle = FRT1 + pos2move
        kit.servo[6].angle = BLT1 - pos2move
        kit.servo[9].angle = BRT1 + pos2move
        pos2move += Pos3TIncrement
        kit.servo[2].angle = FLH
        kit.servo[5].angle = FRH
        kit.servo[8].angle = BLH
        kit.servo[11].angle = BRH  
        time.sleep(Posdelay)

if __name__ == "__main__":
    main()