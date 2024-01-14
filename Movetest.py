from math import sin, cos
from pylx16a.lx16a import *
import time
import pygame
import servoresetmodule

LX16A.initialize("/dev/ttyUSB0", 0.1)

pygame.init()
joy1 = pygame.joystick.Joystick(0)
joy1.init()

servo1 = LX16A(1)
servo2 = LX16A(2)
servo3 = LX16A(3)
servo4 = LX16A(4)
servo5 = LX16A(5)
servo6 = LX16A(6)
servo7 = LX16A(7)
servo8 = LX16A(8)
servo9 = LX16A(9)
servo10 = LX16A(10)
servo11 = LX16A(11)
servo12 = LX16A(12)

servoresetmodule.resetservo(servo1,servo2,servo3,servo4,servo5,servo6,servo7,servo8,servo9,servo10,servo11,servo12)

stop = 0
while stop == 0:
    try:
        pygame.event.pump()

        buttons = [joy1.get_button(0), joy1.get_button(1),joy1.get_button(2),joy1.get_button(3),joy1.get_button(4), joy1.get_button(5)]
        print("buttons: ", buttons)
        axis = [joy1.get_axis(0),joy1.get_axis(1),joy1.get_axis(2),joy1.get_axis(3),joy1.get_axis(4),joy1.get_axis(5)]
        print("axis: ", axis)


        servo1angle = servo1.get_physical_angle()
        servo2angle = servo2.get_physical_angle()
        servo3angle = servo3.get_physical_angle()
        servo4angle = servo4.get_physical_angle()
        servo5angle = servo5.get_physical_angle()
        servo6angle = servo6.get_physical_angle()
        servo7angle = servo7.get_physical_angle()
        servo8angle = servo8.get_physical_angle()
        servo9angle = servo9.get_physical_angle()
        servo10angle = servo10.get_physical_angle()
        servo11angle = servo11.get_physical_angle()
        servo12angle = servo12.get_physical_angle()
      
        heightup = joy1.get_button(3)
        heightdown = joy1.get_button(0)
        movetime = 1000

        if heightup == 1:
            print("Height up")
            servo1angle += 10
            servo4angle -= 10
            servo7angle -= 10
            servo10angle += 10

            print("moving servo1angle to: ", servo1angle)
            print("moving servo4angle to: ", servo4angle)
            print("moving servo7angle to: ", servo7angle)
            print("moving servo10angle to: ", servo10angle)

            servo1.move(servo1angle,movetime,False,False)
            servo4.move(servo4angle,movetime,False,False)
            servo7.move(servo7angle,movetime,False,False)
            servo10.move(servo10angle,movetime,False,False)
        
        if heightdown == 1:
            print("height down")
            servo1angle -= 10
            servo4angle += 10
            servo7angle += 10
            servo10angle -= 10

            print("moving servo1angle to: ", servo1angle)
            print("moving servo4angle to: ", servo4angle)
            print("moving servo7angle to: ", servo7angle)
            print("moving servo10angle to: ", servo10angle)

            servo1.move(servo1angle,movetime,False,False)
            servo4.move(servo4angle,movetime,False,False)
            servo7.move(servo7angle,movetime,False,False)
            servo10.move(servo10angle,movetime,False,False) 
  


        servo1angle = servo1.get_physical_angle()
        print("servo1angle: ", servo1angle )
        servo2angle = servo2.get_physical_angle()
        print("servo2angle: ", servo2angle )
        servo3angle = servo3.get_physical_angle()
        print("servo3angle: ", servo3angle )
        servo4angle = servo4.get_physical_angle()
        print("servo4angle: ", servo4angle )
        servo5angle = servo5.get_physical_angle()
        print("servo5angle: ", servo5angle )
        servo6angle = servo6.get_physical_angle()
        print("servo6angle: ", servo6angle )
        servo7angle = servo7.get_physical_angle()
        print("servo7angle: ", servo7angle )
        servo8angle = servo8.get_physical_angle()
        print("servo8angle: ", servo8angle )
        servo9angle = servo9.get_physical_angle()
        print("servo9angle: ", servo9angle )
        servo10angle = servo10.get_physical_angle()
        print("servo10angle: ", servo10angle )
        servo11angle = servo11.get_physical_angle()
        print("servo11angle: ", servo11angle )
        servo12angle = servo12.get_physical_angle()
        print("servo12angle: ", servo12angle )

        # time.sleep(3)

        stop = joy1.get_button(5)

    finally:
        if stop == 1:
            print("STOP")