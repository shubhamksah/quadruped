import time
import pygame
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

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

def stand(FL1,FL2,FL3,FR1,FR2,FR3,BL1,BL2,BL3,BR1,BR2,BR3):

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


def rest(FL1,FL2,FL3,FR1,FR2,FR3,BL1,BL2,BL3,BR1,BR2,BR3):

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

    FLT_angle = 50
    FLF_angle = 150
    FLH_angle = 90
    FRT_angle = 50
    FRF_angle = 150
    FRH_angle = 90
    BLT_angle = 130
    BLF_angle = 30
    BLH_angle = 90
    BRT_angle = 130
    BRF_angle = 30
    BRH_angle = 90


    
t = 0

try:

    stand(0,1,2,3,4,5,6,7,8,9,10,11,12)

    pygame.init()
    joy1 = pygame.joystick.Joystick(0)
    joy1.init()

    while t == 0:
        try:
            pygame.event.pump()
            buttons = [joy1.get_button(0),joy1.get_button(1),joy1.get_button(2),joy1.get_button(3),joy1.get_button(4),joy1.get_button(5)]
            axis = [joy1.get_axis(0),joy1.get_axis(1),joy1.get_axis(2),joy1.get_axis(3),joy1.get_axis(4),joy1.get_axis(5)]

            if joy1.get_axis(1) < -0.5:

                tpos = 90
                tvar = 5
                tmove = tpos + tvar

                time.sleep(0.05)

            if joy1.get_axis(1) > 0.5:

                time.sleep(0.05)

            if joy1.get_axis(2) < -0.5:

                time.sleep(0.05)

            if joy1.get_axis(2) > 0.5:

                time.sleep(0.05)

            if joy1.get_axis(3) > 0.5:
             
                time.sleep(0.05)

            if joy1.get_axis(3) < -0.5:
     
                time.sleep(0.05)

            if joy1.get_button(1) > 0.5:

                rest(1,2,3,4,5,6,7,8,9,10,11,12)
                time.sleep(0.05)
            
            if joy1.get_button(3) > 0.5:
                
                stand(1,2,3,4,5,6,7,8,9,10,11,12)
                time.sleep(0.05)

            t = joy1.get_button(0)

        finally:
            if t == 1:
                print("STOP")
                rest(0,1,2,3,4,5,6,7,8,9,10,11)

    
except:
    print("Exit")
    quit()