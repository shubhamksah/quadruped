import time
import pygame
from adafruit_servokit import ServoKit

FLT = 88
FLF = 137
FLH = 100

#Position Down = Tibia (7 Down), Femur (42 Back) (35,75)

#Position Back = Tibia (48 Up), Femur (70 Back) (-10,77)

#Position Up = Tibia (26 Up), Femur (72 Back) (12,60)

kit = ServoKit(channels=16)

def main():

    t = 0

    while t <= 0.05: 
        
        try:

            kit.servo[0].angle = 88
            kit.servo[1].angle = 84 + 45
            kit.servo[2].angle = 100

            # kit.servo[2].angle = FLH
            
            # kit.servo[0].angle = FLT + 26 #Up
            # kit.servo[1].angle = FLF + 27 #Up

            # print("Position 1")
            # time.sleep(2)

            # kit.servo[2].angle = FLH

            # kit.servo[0].angle = FLT + 26 #Up
            # kit.servo[1].angle = FLF + 27 #Up

            # print("Position 2")
            # time.sleep(2)

            # kit.servo[2].angle = FLH
            # kit.servo[0].angle = FLT - 7 #Down
            # kit.servo[1].angle = FLF - 3 #Down

            # print("Position 3")
            # time.sleep(2)

            # kit.servo[2].angle = FLH

            # pos1move = 1.5625
            # pos2move = 3
            # while pos2move <= 48:
            #     kit.servo[1].angle = FLF + pos1move
            #     pos1move += 1.5625
            #     kit.servo[0].angle = FLT + pos2move
            #     pos2move += 3
            #     time.sleep(0.0025)


            print("Position 4")
            time.sleep(2)

            t += 0.05
            
        finally:
            if t==1.05:
                print ("STOP")
                kit.servo[0].angle = 90
                kit.servo[1].angle = 90
                kit.servo[2].angle = 100


if __name__ == "__main__":
    main()