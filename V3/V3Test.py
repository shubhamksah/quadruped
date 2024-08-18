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
Pos2F = 10 #Femur Movement in Position 2

Pos3T = 35 #Tibia Movement in Position 3
Pos3F = 20 #Femur Movement in Position 3

Pos2TIncrement = Pos2T/80 #Tibia Movement Increment Position 2
Pos2FIncrement = Pos2F/80 #Femur Movement Increment Position 2

Pos3TIncrement = Pos3T/80 #Tibia Movement Increment Position 3
Pos3FIncrement = Pos3F/80 #Femur Movement Increment Position 3

Pos2delay = 0.000000001 #Position 2 Speed (Lower = Faster)
Pos3delay = 0.000000001 #Position 3 Speed (Lower = Faster)

MovementDelay = 0.0 #Full Movement Speed (Lower = Faster)


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

    kit.servo[2].angle = FLH
    kit.servo[5].angle = FRH
    kit.servo[8].angle = BLH
    kit.servo[11].angle = BRH 

    kit.servo[0].angle = FLT + 12 + 30
    kit.servo[1].angle = FLF + 9 + 12

    kit.servo[3].angle = FRT - 10 - 30
    kit.servo[4].angle = FRF - 9 - 12

    kit.servo[6].angle = BLT + 10 + 30
    kit.servo[7].angle = BLF + 10 + 12

    kit.servo[9].angle = BRT - 10 - 30
    kit.servo[10].angle = BRF - 10 - 12



    # pos3move = Pos3FIncrement
    # pos4move = Pos3TIncrement
    # while pos4move <= Pos3T: 
    #     kit.servo[1].angle = FLF1 + pos3move
    #     kit.servo[4].angle = FRF1 - pos3move
    #     kit.servo[7].angle = BLF1 + pos3move
    #     kit.servo[10].angle = BRF1 - pos3move
    #     pos3move += Pos3FIncrement
    #     kit.servo[0].angle = FLT1 + pos4move
    #     kit.servo[3].angle = FRT1 - pos4move
    #     kit.servo[6].angle = BLT1 + pos4move
    #     kit.servo[9].angle = BRT1 - pos4move
    #     pos4move += Pos3TIncrement
    #     kit.servo[2].angle = FLH
    #     kit.servo[5].angle = FRH
    #     kit.servo[8].angle = BLH
    #     kit.servo[11].angle = BRH  
    #     time.sleep(Pos3delay)

    # time.sleep(2)

    # pos1move = Pos2FIncrement
    # pos2move = Pos2TIncrement
    # while pos2move <= Pos2T: 
    #     kit.servo[1].angle = FLF1 + pos1move
    #     kit.servo[4].angle = FRF1 - pos1move
    #     kit.servo[7].angle = BLF1 + pos1move
    #     kit.servo[10].angle = BRF1 - pos1move
    #     pos1move += Pos2FIncrement
    #     kit.servo[0].angle = FLT1 + pos2move
    #     kit.servo[3].angle = FRT1 - pos2move
    #     kit.servo[6].angle = BLT1 + pos2move
    #     kit.servo[9].angle = BRT1 - pos2move
    #     pos2move += Pos2TIncrement
    #     kit.servo[2].angle = FLH
    #     kit.servo[5].angle = FRH
    #     kit.servo[8].angle = BLH
    #     kit.servo[11].angle = BRH  
    #     time.sleep(Pos2delay)


if __name__ == "__main__":
    main()