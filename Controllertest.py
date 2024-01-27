from pylx16a.lx16a import *
import pygame
import time
import subprocess

def standing_position(FL_TIBIA,FL_FEMUR,FL_HIP,FR_TIBIA,FR_FEMUR,FR_HIP,BR_TIBIA,BR_FEMUR,BR_HIP,BL_TIBIA,BL_FEMUR,BL_HIP):

    FL_TIBIA.move(125,1000,False,False)
    FL_FEMUR.move(143,1000,False,False)
    FL_HIP.move(121.5,1000,False,False)
    FR_TIBIA.move(120,1000,False,False)
    FR_FEMUR.move(115,1000,False,False)
    FR_HIP.move(124,1000,False,False)
    BR_TIBIA.move(105,1000,False,False)
    BR_FEMUR.move(152,1000,False,False)
    BR_HIP.move(115,1000,False,False)
    BL_TIBIA.move(141,1000,False,False)
    BL_FEMUR.move(126,1000,False,False)
    BL_HIP.move(141,1000,False,False)

    print("Standing")

def resting_position(FL_TIBIA,FL_FEMUR,FL_HIP,FR_TIBIA,FR_FEMUR,FR_HIP,BR_TIBIA,BR_FEMUR,BR_HIP,BL_TIBIA,BL_FEMUR,BL_HIP):
    
    FL_TIBIA.move(85.52,1000,False,False)
    FL_FEMUR.move(169.92,1000,False,False)
    FL_HIP.move(121.92,1000,False,False)
    FR_TIBIA.move(161.44,1000,False,False)
    FR_FEMUR.move(84.72,1000,False,False)
    FR_HIP.move(124.08,1000,False,False)
    BR_TIBIA.move(154.24,1000,False,False)
    BR_FEMUR.move(122.4,1000,False,False)
    BR_HIP.move(110.88,1000,False,False)
    BL_TIBIA.move(91.52,1000,False,False)
    BL_FEMUR.move(153.12,1000,False,False)
    BL_HIP.move(141.84,1000,False,False)

    print("Resting")

t = 0

pygame.init()
joy1 = pygame.joystick.Joystick(0)
joy1.init()

LX16A.initialize("/dev/ttyUSB0", 0.1)

try:

    FL_TIBIA = LX16A(1)
    FL_FEMUR = LX16A(2)
    FL_HIP = LX16A(3)
    FR_TIBIA = LX16A(4)
    FR_FEMUR = LX16A(5)
    FR_HIP = LX16A(6)
    BR_TIBIA = LX16A(7)
    BR_FEMUR = LX16A(8)
    BR_HIP = LX16A(9)
    BL_TIBIA = LX16A(10)
    BL_FEMUR = LX16A(11)
    BL_HIP = LX16A(12)
    
    while t == 0:
        try:
            pygame.event.pump()
            buttons = [joy1.get_button(0),joy1.get_button(1),joy1.get_button(2),joy1.get_button(3),joy1.get_button(4),joy1.get_button(5)]
            axis = [joy1.get_axis(0),joy1.get_axis(1),joy1.get_axis(2),joy1.get_axis(3),joy1.get_axis(4),joy1.get_axis(5)]
            pygame.time.Clock().tick(0)
            subprocess.call ("clear")

            tibia = joy1.get_axis(0)
            if tibia < -0.5 :
                FL_TIBIA.move(10,1000,True,False)

            stop=joy1.get_button(0)

        finally:
            if t == 1:
                print("STOP")

    
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()