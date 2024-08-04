import time
import pygame
from adafruit_servokit import ServoKit

FLT = 88
FLF = 137
FLH = 100
FRT = 84
FRF = 42
FRH = 88
BLT = 100
BLF = 131
BLH = 95
BRT = 93
BRF = 41
BRH = 95 

#Position Down = Tibia (7 Down), Femur (42 Back) (35,75)

#Position Back = Tibia (48 Up), Femur (70 Back) (-10,77)

#Position Up = Tibia (26 Up), Femur (72 Back) (12,60)

kit = ServoKit(channels=16)

def main():

    t = 0

    while t <= 1.1: 
        
        try:
            # kit.servo[0].angle = FLT + 26 #Up
            # kit.servo[1].angle = FLF + 27 #Up
            # kit.servo[2].angle = FLH 
            # kit.servo[3].angle = FRT + 7 #Down
            # kit.servo[4].angle = FRF + 3 #Down
            # kit.servo[5].angle = FRH
            # kit.servo[6].angle = BLT - 7 #Down
            # kit.servo[7].angle = BLF - 3 #Down
            # kit.servo[8].angle = BLH 
            # kit.servo[9].angle = BRT - 26 #Up
            # kit.servo[10].angle = BRF - 27 #Up
            # kit.servo[11].angle = BRH    

            # print("Position 1")
            # time.sleep(0.2)

            # kit.servo[0].angle = FLT + 26 #Up
            # kit.servo[1].angle = FLF + 27 #Up
            # kit.servo[2].angle = FLH 
            # kit.servo[3].angle = FRT - 48 #Back
            # kit.servo[4].angle = FRF - 25 #Back
            # kit.servo[5].angle = FRH
            # kit.servo[6].angle = BLT + 48 #Back
            # kit.servo[7].angle = BLF + 25 #Back
            # kit.servo[8].angle = BLH
            # kit.servo[9].angle = BRT - 26 #Up
            # kit.servo[10].angle = BRF - 27 #Up
            # kit.servo[11].angle = BRH 

            # print("Position 2")
            # time.sleep(0.2)

            kit.servo[2].angle = FLH
            kit.servo[5].angle = FRH
            kit.servo[8].angle = BLH
            kit.servo[11].angle = BRH 

            kit.servo[3].angle = FRT - 26 #Up
            kit.servo[4].angle = FRF - 27 #Up
            kit.servo[6].angle = BLT + 26 #Up
            kit.servo[7].angle = BLF + 27 #Up


            kit.servo[0].angle = FLT - 7 #Down
            kit.servo[1].angle = FLF - 3 #Down

            kit.servo[9].angle = BRT + 7 #Down
            kit.servo[10].angle = BRF + 3 #Down

            print("Position 3")
            time.sleep(2)



            kit.servo[3].angle = FRT - 26 #Up
            kit.servo[4].angle = FRF - 27 #Up

            kit.servo[6].angle = BLT + 26 #Up
            kit.servo[7].angle = BLF + 27 #Up


            kit.servo[0].angle = FLT + 24  #Back
            kit.servo[9].angle = BRT - 24 #Back
            time.sleep(1)
            kit.servo[1].angle = FLF + 10 #Back
            kit.servo[10].angle = BRF - 10 #Back
            time.sleep(0.1)
            kit.servo[1].angle = FLF + 15 #Back
            kit.servo[10].angle = BRF - 15 #Back          
            time.sleep(1)
            kit.servo[0].angle = FLT + 24  #Back
            kit.servo[9].angle = BRT - 24 #Back


            print("Position 4")
            time.sleep(2)

            t += 0.05
            
        finally:
            if t==1:
                print ("STOP")
                kit.servo[0].angle = 50
                kit.servo[1].angle = 150
                kit.servo[2].angle = 100
                kit.servo[3].angle = 137
                kit.servo[4].angle = 35
                kit.servo[5].angle = 88
                kit.servo[6].angle = 48
                kit.servo[7].angle = 145
                kit.servo[8].angle = 95
                kit.servo[9].angle = 134
                kit.servo[10].angle = 30
                kit.servo[11].angle = 95 


if __name__ == "__main__":
    main()