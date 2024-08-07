import time
import pygame
from adafruit_servokit import ServoKit

#Default Standing

FLT = 88
FLF = 129
FLH = 100

FRT = 82
FRF = 45
FRH = 88

BLT = 100
BLF = 131
BLH = 95

BRT = 93
BRF = 41
BRH = 95 

#Position 2 Default

FLT1 = FLT - 20
FLF1 = FLF - 13

FRT1 = FRT + 20
FRF1 = FRF + 13

BLT1 = BLT - 20
BLF1 = BLF - 13

BRT1 = BRT + 20
BRF1 = BRF + 13

#Variables

Pos1T = 20 #Position 1 Tibia Movement Down
Pos1F = 13 #Position 1 Femur Movement Forward
Pos3T = 3 #Position 3 Tibia Movement from Default

Pos2T = 66 #Tibia Movement in Position 2
Pos2F = 37 #Femur Movement in Position 2

Pos2TIncrement = Pos2T/160 #Tibia Movement Increment Position 2
Pos2FIncrement = Pos2F/160 #Femur Movement Increment Position 2

Pos2delay = 0.00001 #Position 2 Speed (Lower = Faster)

MovementDelay = 0.1 #Full Movement Speed (Lower = Faster)


#Position Down = Tibia (20 Down), Femur (13 Forward)

#Position Back = Tibia (66 Up + last pos), Femur (37 Back + last pos)

#Position Up = Tibia (90 - 3 Down)

kit = ServoKit(channels=16) #Initializes Servos

def main():

    t = 0

    while t <= 2.05: #Movement Loop
        
        try:

            t += 0.05
            
        finally:
            if t==2.05:
                print ("STOP") #Default Position Reset
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


if __name__ == "__main__":
    main()