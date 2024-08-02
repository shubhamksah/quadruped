import time
import pygame
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def stand(FL1,FL2,FL3,FR1,FR2,FR3,BL1,BL2,BL3,BR1,BR2,BR3):

    kit.servo[FL1].angle = 90
    kit.servo[FL2].angle = 90
    kit.servo[FL3].angle = 90
    kit.servo[FR1].angle = 90
    kit.servo[FR2].angle = 90
    kit.servo[FR3].angle = 90
    kit.servo[BL1].angle = 90
    kit.servo[BL2].angle = 90
    kit.servo[BL3].angle = 90
    kit.servo[BR1].angle = 90
    kit.servo[BR2].angle = 90
    kit.servo[BR3].angle = 90  

def rest(FL1,FL2,FL3,FR1,FR2,FR3,BL1,BL2,BL3,BR1,BR2,BR3):

    kit.servo[FL1].angle = 90
    kit.servo[FL2].angle = 125
    kit.servo[FL3].angle = 85
    kit.servo[FR1].angle = 90
    kit.servo[FR2].angle = 50
    kit.servo[FR3].angle = 90
    kit.servo[BL1].angle = 90
    kit.servo[BL2].angle = 135
    kit.servo[BL3].angle = 95
    kit.servo[BR1].angle = 90
    kit.servo[BR2].angle = 40
    kit.servo[BR3].angle = 95  

    
t = 0

try:

    stand(1,2,3,4,5,6,7,8,9,10,11,12)

    pygame.init()
    joy1 = pygame.joystick.Joystick(0)
    joy1.init()

    while t == 0:
        try:
            pygame.event.pump()
            buttons = [joy1.get_button(0),joy1.get_button(1),joy1.get_button(2),joy1.get_button(3),joy1.get_button(4),joy1.get_button(5)]
            axis = [joy1.get_axis(0),joy1.get_axis(1),joy1.get_axis(2),joy1.get_axis(3),joy1.get_axis(4),joy1.get_axis(5)]

            if joy1.get_axis(1) < -0.5:

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
            
            if joy1.get_button(3) > 0.5:
                
                stand(1,2,3,4,5,6,7,8,9,10,11,12)

            t = joy1.get_button(0)

        finally:
            if t == 1:
                print("STOP")
                rest(1,2,3,4,5,6,7,8,9,10,11,12)

    
except:
    print("Exit")
    quit()