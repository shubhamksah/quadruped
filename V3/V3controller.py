import time
import pygame
from adafruit_servokit import ServoKit

# Initializing servo angle variables
FLT_angle = 90
FLF_angle = 90
FLH_angle = 90
FRT_angle = 90
FRF_angle = 90
FRH_angle = 90
BLT_angle = 90
BLF_angle = 90
BLH_angle = 90
BRT_angle = 90
BRF_angle = 90
BRH_angle = 90

def main():
    print("Running Quadruped")

    kit = ServoKit(channels=16)
        
    global FLT_angle
    global FLF_angle
    global FLH_angle
    global FRT_angle
    global FRF_angle
    global FRH_angle
    global BLT_angle
    global BLF_angle
    global BLH_angle
    global BRT_angle 
    global BRF_angle 
    global BRH_angle

    stand(kit)

    t = 0

    pygame.init()
    joy1 = pygame.joystick.Joystick(0)
    joy1.init()

    while t == 0:
        try:
            pygame.event.pump()
            buttons = [joy1.get_button(0),joy1.get_button(1),joy1.get_button(2),joy1.get_button(3),joy1.get_button(4),joy1.get_button(5)]
            axis = [joy1.get_axis(0),joy1.get_axis(1),joy1.get_axis(2),joy1.get_axis(3),joy1.get_axis(4),joy1.get_axis(5)]

            if joy1.get_axis(1) < -0.5:

                FLT_move = FLT_angle + 2
                FRT_move = FRT_angle - 2
                BLT_move = BLT_angle + 2
                BRT_move = BRT_angle - 2
                
                FLT_angle = FLT_move
                FRT_angle = FRT_move
                BLT_angle = BLT_move
                BRT_angle = BRT_move

                kit.servo[0].angle = FLT_move
                kit.servo[3].angle = FRT_move
                kit.servo[6].angle = BLT_move
                kit.servo[9].angle = BRT_move

                time.sleep(0.05)

            if joy1.get_axis(1) > 0.5:

                FLT_move = FLT_angle - 2
                FRT_move = FRT_angle + 2
                BLT_move = BLT_angle - 2
                BRT_move = BRT_angle + 2
                
                FLT_angle = FLT_move
                FRT_angle = FRT_move
                BLT_angle = BLT_move
                BRT_angle = BRT_move

                kit.servo[0].angle = FLT_move
                kit.servo[3].angle = FRT_move
                kit.servo[6].angle = BLT_move
                kit.servo[9].angle = BRT_move

                time.sleep(0.05)

            if joy1.get_axis(2) < -0.5:

                FLF_move = FLF_angle - 2
                FRF_move = FRF_angle + 2
                BLF_move = BLF_angle - 2
                BRF_move = BRF_angle + 2
                
                FLF_angle = FLF_move
                FRF_angle = FRF_move
                BLF_angle = BLF_move
                BRF_angle = BRF_move

                kit.servo[1].angle = FLF_move
                kit.servo[4].angle = FRF_move
                kit.servo[7].angle = BLF_move
                kit.servo[10].angle = BRF_move

                time.sleep(0.05)

            if joy1.get_axis(2) > 0.5:

                FLF_move = FLF_angle + 2
                FRF_move = FRF_angle - 2
                BLF_move = BLF_angle + 2
                BRF_move = BRF_angle - 2
                
                FLF_angle = FLF_move
                FRF_angle = FRF_move
                BLF_angle = BLF_move
                BRF_angle = BRF_move

                kit.servo[1].angle = FLF_move
                kit.servo[4].angle = FRF_move
                kit.servo[7].angle = BLF_move
                kit.servo[10].angle = BRF_move

                time.sleep(0.05)

            if joy1.get_axis(3) > 0.5:
            
                FLH_move = FLH_angle + 2
                FRH_move = FRH_angle - 2
                BLH_move = BLH_angle + 2
                BRH_move = BRH_angle - 2
                
                FLH_angle = FLH_move
                FRH_angle = FRH_move
                BLH_angle = BLH_move
                BRH_angle = BRH_move

                kit.servo[2].angle = FLH_move
                kit.servo[5].angle = FRH_move
                kit.servo[8].angle = BLH_move
                kit.servo[11].angle = BRH_move
            
                time.sleep(0.05)

            if joy1.get_axis(3) < -0.5:
    
                FLH_move = FLH_angle - 2
                FRH_move = FRH_angle + 2
                BLH_move = BLH_angle - 2
                BRH_move = BRH_angle + 2
                
                FLH_angle = FLH_move
                FRH_angle = FRH_move
                BLH_angle = BLH_move
                BRH_angle = BRH_move

                kit.servo[2].angle = FLH_move
                kit.servo[5].angle = FRH_move
                kit.servo[8].angle = BLH_move
                kit.servo[11].angle = BRH_move

                time.sleep(0.05)

            if joy1.get_button(1) > 0.5:

                rest(kit)
                time.sleep(0.05)
            
            if joy1.get_button(3) > 0.5:
                
                stand(kit)
                time.sleep(0.05)

            t = joy1.get_button(0)

        finally:
            if t == 1:
                print("STOP")
                rest(kit)


def stand(kit):

    kit.servo[0].angle = 90
    kit.servo[1].angle = 135
    kit.servo[2].angle = 100
    kit.servo[3].angle = 97
    kit.servo[4].angle = 45
    kit.servo[5].angle = 88
    kit.servo[6].angle = 88
    kit.servo[7].angle = 130
    kit.servo[8].angle = 95
    kit.servo[9].angle = 94
    kit.servo[10].angle = 45
    kit.servo[11].angle = 95  

    global FLT_angle
    global FLF_angle
    global FLH_angle
    global FRT_angle
    global FRF_angle
    global FRH_angle
    global BLT_angle
    global BLF_angle
    global BLH_angle
    global BRT_angle 
    global BRF_angle 
    global BRH_angle  

    FLT_angle = 90
    FLF_angle = 135
    FLH_angle = 100
    FRT_angle = 97
    FRF_angle = 45
    FRH_angle = 88
    BLT_angle = 88
    BLF_angle = 130
    BLH_angle = 95
    BRT_angle = 94
    BRF_angle = 45
    BRH_angle = 95


def rest(kit):

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

    global FLT_angle
    global FLF_angle
    global FLH_angle
    global FRT_angle
    global FRF_angle
    global FRH_angle
    global BLT_angle
    global BLF_angle
    global BLH_angle
    global BRT_angle 
    global BRF_angle 
    global BRH_angle     
    
    FLT_angle = 50
    FLF_angle = 150
    FLH_angle = 100
    FRT_angle = 137
    FRF_angle = 35
    FRH_angle = 88
    BLT_angle = 48
    BLF_angle = 145
    BLH_angle = 95
    BRT_angle = 134
    BRF_angle = 30
    BRH_angle = 95  

if __name__ == "__main__":
    main()