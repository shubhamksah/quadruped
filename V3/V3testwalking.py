import time
import pygame
from adafruit_servokit import ServoKit

FLT = 88
FLF = 129
FLH = 100

#Position Down = Tibia (35 Down), Femur (36 Back) (40,60)

#Position Back = Tibia (50 Up), Femur (84 Back) (0,60)

#Position Up = Tibia (18 Down), Femur (63 Back) (30,40)

kit = ServoKit(channels=16)

def main():

    t = 0

    while t <= 2.05: 
        
        try:

            kit.servo[0].angle = 84
            kit.servo[1].angle = 129
            kit.servo[2].angle = 100

            time.sleep(3)

            pos1move = 1.6
            pos2move = 3.2
            while pos2move <= 38:
                kit.servo[1].angle = FLF + pos1move
                pos1move += 1.6
                kit.servo[0].angle = FLT + pos2move
                pos2move += 3.8
                time.sleep(0.005)

            time.sleep(3)  

            kit.servo[0].angle = 85

            time.sleep(3)

            # kit.servo[0].angle = 88 - 35
            # kit.servo[1].angle = 120
            # kit.servo[2].angle = 100

            # time.sleep(1)

            # pos1move = 4.5
            # pos2move = 3
            # while pos1move <= 43:
            #     kit.servo[1].angle = FLF + pos1move
            #     pos1move += 4.3
            #     kit.servo[0].angle = FLT + pos2move
            #     pos2move += 2.6
            #     time.sleep(0.005)

            # # kit.servo[0].angle = 88 + 50
            # # kit.servo[1].angle = 129 + 39
            # # kit.servo[2].angle = 100

            # time.sleep(1)

            # kit.servo[0].angle = 88 - 18
            # kit.servo[1].angle = 129 + 18
            # kit.servo[2].angle = 100

            # time.sleep(3)

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
            if t==2.05:
                print ("STOP")
                # kit.servo[0].angle = 88
                # kit.servo[1].angle = 129
                # kit.servo[2].angle = 100


if __name__ == "__main__":
    main()