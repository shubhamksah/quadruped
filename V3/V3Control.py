import time
import pygame
from adafruit_servokit import ServoKit

# Initializing servo angle variables
FLH_angle = 100
FRH_angle = 88
BLH_angle = 95
BRH_angle = 95 
FLT_angle = 90
FLF_angle = 140
FRT_angle = 90
FRF_angle = 45
BLT_angle = 87
BLF_angle = 130
BRT_angle = 85
BRF_angle = 43


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

    kit.servo[0].angle = FLT_angle
    kit.servo[1].angle = FLF_angle
    kit.servo[2].angle = FLH_angle
    kit.servo[3].angle = FRT_angle
    kit.servo[4].angle = FRF_angle
    kit.servo[5].angle = FRH_angle
    kit.servo[6].angle = BLT_angle
    kit.servo[7].angle = BLF_angle
    kit.servo[8].angle = BLH_angle
    kit.servo[9].angle = BRT_angle
    kit.servo[10].angle = BRF_angle
    kit.servo[11].angle = BRH_angle
    
    t = 0

    pygame.init()
    joy1 = pygame.joystick.Joystick(0)
    joy1.init()

    while t == 0:
        try:
            pygame.event.pump()
            buttons = [joy1.get_button(0),joy1.get_button(1),joy1.get_button(2),joy1.get_button(3),joy1.get_button(4),joy1.get_button(5)]
            axis = [joy1.get_axis(0),joy1.get_axis(1),joy1.get_axis(2),joy1.get_axis(3),joy1.get_axis(4),joy1.get_axis(5)]

            if joy1.get_axis(1) < -0.5: #Tibia Up

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

            if joy1.get_axis(1) > 0.5: #Tibia Down

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

            if joy1.get_axis(2) < -0.5: #Femur Forward

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

            if joy1.get_axis(2) > 0.5: #Femur Back

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
            
                FLH_move = FLH_angle - 2
                FRH_move = FRH_angle - 2
                BLH_move = BLH_angle + 2
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

            if joy1.get_axis(3) < -0.5:
    
                FLH_move = FLH_angle + 2
                FRH_move = FRH_angle + 2
                BLH_move = BLH_angle - 2
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

            # if joy1.get_button(1) > 0.5:

            #     rest(kit)
            #     time.sleep(0.05)
            
            if joy1.get_button(3) > 0.5:
                
                stand(kit)
                time.sleep(0.05)

            t = joy1.get_button(0)

        finally:
            if t == 1:
                print("STOP")


def stand(kit):

    kit.servo[0].angle = 90
    kit.servo[1].angle = 140
    kit.servo[2].angle = 100
    kit.servo[3].angle = 90
    kit.servo[4].angle = 45
    kit.servo[5].angle = 88
    kit.servo[6].angle = 87
    kit.servo[7].angle = 130
    kit.servo[8].angle = 95
    kit.servo[9].angle = 85
    kit.servo[10].angle = 43
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

    FLH_angle = 100
    FRH_angle = 88
    BLH_angle = 95
    BRH_angle = 95 
    FLT_angle = 90
    FLF_angle = 140
    FRT_angle = 90
    FRF_angle = 45
    BLT_angle = 87
    BLF_angle = 130
    BRT_angle = 85
    BRF_angle = 43


# def rest(kit):

#     kit.servo[0].angle = 50
#     kit.servo[1].angle = 150
#     kit.servo[2].angle = 100
#     kit.servo[3].angle = 137
#     kit.servo[4].angle = 35
#     kit.servo[5].angle = 88
#     kit.servo[6].angle = 48
#     kit.servo[7].angle = 145
#     kit.servo[8].angle = 95
#     kit.servo[9].angle = 134
#     kit.servo[10].angle = 30
#     kit.servo[11].angle = 95  

#     global FLT_angle
#     global FLF_angle
#     global FLH_angle
#     global FRT_angle
#     global FRF_angle
#     global FRH_angle
#     global BLT_angle
#     global BLF_angle
#     global BLH_angle
#     global BRT_angle 
#     global BRF_angle 
#     global BRH_angle     
    
#     FLT_angle = 50
#     FLF_angle = 150
#     FLH_angle = 100
#     FRT_angle = 137
#     FRF_angle = 35
#     FRH_angle = 88
#     BLT_angle = 48
#     BLF_angle = 145
#     BLH_angle = 95
#     BRT_angle = 134
#     BRF_angle = 30
#     BRH_angle = 95  

if __name__ == "__main__":
    main()