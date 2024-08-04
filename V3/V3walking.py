import time
import pygame
from adafruit_servokit import ServoKit

FLT = 90
FLF = 135
FLH = 100
FRT = 97
FRF = 45
FRH = 88
BLT = 88
BLF = 130
BLH = 95
BRT = 94
BRF = 45
BRH = 95 

#Position Down = Tibia (0), Femur (45 Back)
#Position Back = Tibia (33 Up), Femur (63 Back)
#Position Up = Tibia (30 Up), Femur (74 Back)

kit = ServoKit(channels=16)

def main():

    t = 0

    while t == 0: 
        
        try:
            kit.servo[0].angle = FLT + 30 #Up
            kit.servo[1].angle = FLF + 29 #Up
            kit.servo[2].angle = FLH 
            kit.servo[3].angle = FRT + 0 #Down
            kit.servo[4].angle = FRF + 0 #Down
            kit.servo[5].angle = FRH
            kit.servo[6].angle = BLT + 0 #Down
            kit.servo[7].angle = BLF + 0 #Down
            kit.servo[8].angle = BLH 
            kit.servo[9].angle = BRT - 30 #Up
            kit.servo[10].angle = BRF - 16 #Up
            kit.servo[11].angle = BRH    

            print("Position 1")
            time.sleep(0.5)

            kit.servo[0].angle = FLT + 30 #Up
            kit.servo[1].angle = FLF + 29 #Up
            kit.servo[2].angle = FLH 
            kit.servo[3].angle = FRT - 33 #Back
            kit.servo[4].angle = FRF - 18 #Back
            kit.servo[5].angle = FRH
            kit.servo[6].angle = BLT + 33 #Back
            kit.servo[7].angle = BLF + 18 #Back
            kit.servo[8].angle = BLH
            kit.servo[9].angle = BRT - 30 #Up
            kit.servo[10].angle = BRF - 16 #Up
            kit.servo[11].angle = BRH 

            print("Position 2")
            time.sleep(0.5)

            kit.servo[0].angle = FLT + 0 #Down
            kit.servo[1].angle = FLF + 0 #Down
            kit.servo[2].angle = FLH
            kit.servo[3].angle = FRT - 30 #Up
            kit.servo[4].angle = FRF - 29 #Up
            kit.servo[5].angle = FRH
            kit.servo[6].angle = BLT + 30 #Up
            kit.servo[7].angle = BLF + 29 #Up
            kit.servo[8].angle = BLH
            kit.servo[9].angle = BRT + 0 #Down
            kit.servo[10].angle = BRF + 0 #Down
            kit.servo[11].angle = BRH 

            print("Position 3")
            time.sleep(0.5)

            kit.servo[0].angle = FLT + 33 #Back
            kit.servo[1].angle = FLF + 29 #Back
            kit.servo[2].angle = FLH
            kit.servo[3].angle = FRT - 30 #Up
            kit.servo[4].angle = FRF - 29 #Up
            kit.servo[5].angle = FRH
            kit.servo[6].angle = BLT + 30 #Up
            kit.servo[7].angle = BLF + 29 #Up
            kit.servo[8].angle = BLH
            kit.servo[9].angle = BRT - 33 #Back
            kit.servo[10].angle = BRF - 29 #Back
            kit.servo[11].angle = BRH 

            print("Position 3")
            time.sleep(0.5)

            t += 0.1
            
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