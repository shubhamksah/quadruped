import time
import pygame
from adafruit_servokit import ServoKit

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

FLT1 = FLT - 20
FLF1 = FLF - 13

FRT1 = FRT + 20
FRF1 = FRF + 13

BLT1 = BLT - 20
BLF1 = BLF - 13

BRT1 = BRT + 20
BRF1 = BRF + 13

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

kit = ServoKit(channels=16)

def main():

    t = 0

    while t <= 2.05: 
        
        try:

            # #FL Movement

            # #Down
            # kit.servo[0].angle = FLT - Pos1T 
            # kit.servo[1].angle = FLF - Pos1F
            # kit.servo[2].angle = FLH 

            # time.sleep(MovementDelay)

            # #Back
            # pos1move = Pos2FIncrement
            # pos2move = Pos2TIncrement
            # while pos2move <= Pos2T: 
            #     kit.servo[1].angle = FLF1 + pos1move
            #     pos1move += Pos2FIncrement
            #     kit.servo[0].angle = FLT1 + pos2move
            #     pos2move += Pos2TIncrement
            #     kit.servo[2].angle = FLH
            #     time.sleep(Pos2delay)

            # time.sleep(MovementDelay)  

            # #Up
            # kit.servo[0].angle = FLT - Pos3T
            # kit.servo[2].angle = FLH

            # time.sleep(MovementDelay)

            # #FR Movement

            # #Down
            # kit.servo[3].angle = FRT + Pos1T
            # kit.servo[4].angle = FRF + Pos1F
            # kit.servo[5].angle = FRH

            # time.sleep(MovementDelay)

            # #Back
            # pos1move = Pos2FIncrement
            # pos2move = Pos2TIncrement
            # while pos2move <= Pos2T:
            #     kit.servo[4].angle = FRF1 - pos1move
            #     pos1move += Pos2FIncrement
            #     kit.servo[3].angle = FRT1 - pos2move
            #     pos2move += Pos2TIncrement
            #     kit.servo[5].angle = FRH
            #     time.sleep(Pos2delay)

            # time.sleep(MovementDelay)  

            # #Up
            # kit.servo[3].angle = FRT - Pos3T
            # kit.servo[5].angle = FRH

            # time.sleep(MovementDelay)

            #BL Movement

            #Down
            kit.servo[6].angle = BLT - Pos1T
            kit.servo[7].angle = BLF - Pos1F
            kit.servo[8].angle = BLH

            time.sleep(MovementDelay)

            #Back
            pos1move = Pos2FIncrement
            pos2move = Pos2TIncrement
            while pos2move <= Pos2T:
                kit.servo[7].angle = BLF1 + pos1move
                pos1move += Pos2FIncrement
                kit.servo[6].angle = BLT1 + pos2move
                pos2move += Pos2TIncrement
                kit.servo[8].angle = BLH
                time.sleep(Pos2delay)

            time.sleep(MovementDelay)  

            #Up
            kit.servo[6].angle = BLT - Pos3T
            kit.servo[8].angle = BLH

            time.sleep(MovementDelay)

            #BR Movement

            #Down
            # kit.servo[9].angle = BRT + Pos1T
            # kit.servo[10].angle = BRF + Pos1F
            # kit.servo[11].angle = BRH

            # time.sleep(MovementDelay)

            # #Back
            # pos1move = Pos2FIncrement
            # pos2move = Pos2TIncrement
            # while pos2move <= Pos2T:
            #     kit.servo[10].angle = BRF1 - pos1move
            #     pos1move += Pos2FIncrement
            #     kit.servo[9].angle = BRT1 - pos2move
            #     pos2move += Pos2TIncrement
            #     kit.servo[11].angle = BRH
            #     time.sleep(Pos2delay)
            

            # time.sleep(MovementDelay)  

            # #Up
            # kit.servo[9].angle = BRT + Pos3T
            # kit.servo[11].angle = BRH

            # time.sleep(MovementDelay)

            t += 0.05
            
        finally:
            if t==2.05:
                print ("STOP")
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