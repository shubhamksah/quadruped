from math import sin, cos
from pylx16a.lx16a import *
import time
import pygame

LX16A.initialize("/dev/ttyUSB0", 0.1)

pygame.init()
joy1 = pygame.joystick.Joystick(0)
joy1.init()

stop = 1
while stop:
    try:
        pygame.event.pump()

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

        buttons = [joy1.get_button(0), joy1.get_button(1),joy1.get_button(2),joy1.get_button(3),joy1.get_button(4), joy1.get_button(0)]
        print("buttons: ", buttons)
        axis = [joy1.get_axis(0),joy1.get_axis(1),joy1.get_axis(2),joy1.get_axis(3),joy1.get_axis(4),joy1.get_axis(5)]
        print("axis: ", axis)

        servo1angle = servo1.get_physical_angle()
        print("sevo1angle: ", servo1angle )
        servo2angle = servo2.get_physical_angle()
        print("sevo2angle: ", servo2angle )
        servo3angle = servo3.get_physical_angle()
        print("sevo3angle: ", servo3angle )
        servo4angle = servo4.get_physical_angle()
        print("sevo4angle: ", servo4angle )
        servo5angle = servo5.get_physical_angle()
        print("sevo5angle: ", servo5angle )
        servo6angle = servo6.get_physical_angle()
        print("sevo6angle: ", servo6angle )
        servo7angle = servo7.get_physical_angle()
        print("sevo7angle: ", servo7angle )
        servo8angle = servo8.get_physical_angle()
        print("sevo8angle: ", servo8angle )
        servo9angle = servo9.get_physical_angle()
        print("sevo9angle: ", servo9angle )
        servo10angle = servo10.get_physical_angle()
        print("sevo10angle: ", servo10angle )
        servo11angle = servo11.get_physical_angle()
        print("sevo11angle: ", servo11angle )
        servo12angle = servo12.get_physical_angle()
        print("sevo12angle: ", servo12angle )

        time.sleep(4)

        stop = joy1.get_button(0) -1

    finally:
        if stop == 0:
            print("STOP")