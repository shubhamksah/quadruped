import time
import pygame
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def standing_position(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve):

    kit.servo[one].angle = 90
    kit.servo[two].angle = 125
    kit.servo[three].angle = 85
    kit.servo[four].angle = 90
    kit.servo[five].angle = 50
    kit.servo[six].angle = 90
    kit.servo[seven].angle = 90
    kit.servo[eight].angle = 135
    kit.servo[nine].angle = 95
    kit.servo[ten].angle = 90
    kit.servo[eleven].angle = 40
    kit.servo[twelve].angle = 95  

def resting_position(one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve):

    kit.servo[one].angle = 60
    kit.servo[two].angle = 125
    kit.servo[three].angle = 85
    kit.servo[four].angle = 120
    kit.servo[five].angle = 50
    kit.servo[six].angle = 90
    kit.servo[seven].angle = 60
    kit.servo[eight].angle = 135
    kit.servo[nine].angle = 95
    kit.servo[ten].angle = 120
    kit.servo[eleven].angle = 40
    kit.servo[twelve].angle = 95  
    
t = 0

try:

    resting_position(1,2,3,4,5,6,7,8,9,10,11,12)

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

                resting_position(1,2,3,4,5,6,7,8,9,10,11,12)
            
            if joy1.get_button(3) > 0.5:
                
                standing_position(1,2,3,4,5,6,7,8,9,10,11,12)

            t = joy1.get_button(0)

        finally:
            if t == 1:
                print("STOP")
                resting_position(1,2,3,4,5,6,7,8,9,10,11,12)

    
except:
    print("Exit")
    quit()