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

BLT1 = 100
BLF1 = 131

BRT1 = 93
BRF1 = 41


#Position Down = Tibia (20 Down), Femur (13 Forward)

#Position Back = Tibia (66 Up + last pos), Femur (37 Back + last pos)

#Position Up = Tibia (90 - 3 Down)

kit = ServoKit(channels=16)

def main():

    t = 0

    while t <= 2.05: 
        
        try:

            #FL Movement

            # kit.servo[0].angle = FLT - 20
            # kit.servo[1].angle = FLF - 13
            # kit.servo[2].angle = FLH

            # time.sleep(0.1)

            # pos1move = 0.23125
            # pos2move = 0.4125
            # while pos2move <= 66:
            #     kit.servo[1].angle = FLF1 + pos1move
            #     pos1move += 0.23125
            #     kit.servo[0].angle = FLT1 + pos2move
            #     pos2move += 0.4125
            #     time.sleep(0.00001)

            # time.sleep(0.1)  

            # kit.servo[0].angle = FLT - 3

            # time.sleep(0.1)

            #FR Movement

            kit.servo[3].angle = FRT + 20
            kit.servo[4].angle = FRF + 13
            kit.servo[5].angle = FRH

            time.sleep(0.1)

            pos1move = 0.23125
            pos2move = 0.4125
            while pos2move <= 66:
                kit.servo[4].angle = FRF1 - pos1move
                pos1move += 0.23125
                kit.servo[3].angle = FRT1 - pos2move
                pos2move += 0.4125
                time.sleep(0.00001)

            time.sleep(0.1)  

            kit.servo[3].angle = FRT + 3

            time.sleep(0.1)


            t += 0.05
            
        finally:
            if t==2.05:
                print ("STOP")
                # kit.servo[0].angle = 88
                # kit.servo[1].angle = 129
                # kit.servo[2].angle = 100


if __name__ == "__main__":
    main()