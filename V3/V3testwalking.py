import time
import pygame
from adafruit_servokit import ServoKit

FLT = 88
FLF = 129
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
            kit.servo[1].angle = 120
            kit.servo[2].angle = 100


            # pos1move = 1.5625
            # pos2move = 3
            # while pos2move <= 48:
            #     kit.servo[1].angle = FLF + pos1move
            #     pos1move += 1.5625
            #     kit.servo[0].angle = FLT + pos2move
            #     pos2move += 3
            #     time.sleep(0.0025)

            t += 0.05
            
        finally:
            if t==1.05:
                print ("STOP")
                kit.servo[0].angle = 88
                kit.servo[1].angle = 129
                kit.servo[2].angle = 100


if __name__ == "__main__":
    main()