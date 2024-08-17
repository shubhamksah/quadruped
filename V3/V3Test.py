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

#Position 2 Default

FLT1 = FLT + 35
FLF1 = FLF + 20

FRT1 = FRT - 35
FRF1 = FRF - 20

BLT1 = BLT + 35
BLF1 = BLF + 20

BRT1 = BRT - 35
BRF1 = BRF - 20

#Variables

Pos2T = 25 #Tibia Movement in Position 2
Pos2F = 15 #Femur Movement in Position 2

Pos2TIncrement = Pos2T/160 #Tibia Movement Increment Position 2
Pos2FIncrement = Pos2F/160 #Femur Movement Increment Position 2

Pos2delay = 0.000000001 #Position 2 Speed (Lower = Faster)

MovementDelay = 0.1 #Full Movement Speed (Lower = Faster)


#Position Down = Tibia (20 Down), Femur (13 Forward)

#Position Back = Tibia (66 Up + last pos), Femur (37 Back + last pos)

#Position Up = Tibia (90 - 3 Down)

kit = ServoKit(channels=16) #Initializes Servos

def main():

    t = 0

    kit.servo[0].angle = FLT
    kit.servo[1].angle = FLF
    kit.servo[2].angle = FLH
    kit.servo[3].angle = FRT
    kit.servo[4].angle = FRF
    kit.servo[5].angle = FRH
    kit.servo[6].angle = BLT
    kit.servo[7].angle = BLF
    kit.servo[8].angle = BLH
    kit.servo[9].angle = BRT
    kit.servo[10].angle = BRF
    kit.servo[11].angle = BRH  

    time.sleep(2)

    kit.servo[1].angle = FLF1
    kit.servo[4].angle = FRF1
    kit.servo[7].angle = BLF1
    kit.servo[10].angle = BRF1

    time.sleep(1)

    kit.servo[0].angle = FLT1
    kit.servo[2].angle = FLH
    kit.servo[3].angle = FRT1
    kit.servo[5].angle = FRH
    kit.servo[6].angle = BLT1
    kit.servo[8].angle = BLH
    kit.servo[9].angle = BRT1
    kit.servo[11].angle = BRH  

    time.sleep(2)

    pos1move = Pos2FIncrement
    pos2move = Pos2TIncrement
    while pos2move <= Pos2T: 
        kit.servo[1].angle = FLF1 + pos1move
        kit.servo[4].angle = FRF1 - pos1move
        kit.servo[7].angle = BLF1 + pos1move
        kit.servo[10].angle = BRF1 - pos1move
        pos1move += Pos2FIncrement
        kit.servo[0].angle = FLT1 + pos2move
        kit.servo[3].angle = FRT1 - pos2move
        kit.servo[6].angle = BLT1 + pos2move
        kit.servo[9].angle = BRT1 - pos2move
        pos2move += Pos2TIncrement
        kit.servo[2].angle = FLH
        kit.servo[5].angle = FRH
        kit.servo[8].angle = BLH
        kit.servo[11].angle = BRH  
        time.sleep(Pos2delay)


    # while t <= 3.05:
    #     try:
    #         #FL Movement

    #         #Down
    #         kit.servo[0].angle = FLT - Pos1T 
    #         kit.servo[1].angle = FLF - Pos1F
    #         kit.servo[2].angle = FLH 

    #         time.sleep(MovementDelay)

    #         #Back
    #         pos1move = Pos2FIncrement
    #         pos2move = Pos2TIncrement
    #         while pos2move <= Pos2T: 
    #             kit.servo[1].angle = FLF1 + pos1move
    #             pos1move += Pos2FIncrement
    #             kit.servo[0].angle = FLT1 + pos2move
    #             pos2move += Pos2TIncrement
    #             kit.servo[2].angle = FLH
    #             time.sleep(Pos2delay)

    #         time.sleep(MovementDelay)  

    #         #Up
    #         kit.servo[0].angle = FLT - Pos3T
    #         kit.servo[2].angle = FLH

    #         time.sleep(MovementDelay)

    #         t += 0.05

    #     finally:
    #         print("STOP")

if __name__ == "__main__":
    main()