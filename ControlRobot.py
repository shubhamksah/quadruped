from pylx16a.lx16a import *
import pygame
import time

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

            if joy1.get_axis(1) < -0.5:
                FR_TIBIA_ANGLE = FR_TIBIA.get_physical_angle()
                BR_TIBIA_ANGLE = BR_TIBIA.get_physical_angle()
                FL_TIBIA.move(5,50,True,False)
                BL_TIBIA.move(5,50,True,False)
                time.sleep(0.07)

            if joy1.get_axis(1) > 0.5:
                FL_TIBIA_ANGLE = FL_TIBIA.get_physical_angle()
                BL_TIBIA_ANGLE = BL_TIBIA.get_physical_angle()
                FL_TIBIA_MOVE = FL_TIBIA_ANGLE - 5
                BL_TIBIA_MOVE = BL_TIBIA_ANGLE - 5
                FL_TIBIA.move(FL_TIBIA_MOVE,25,False,False)
                BL_TIBIA.move(BL_TIBIA_MOVE,25,False,False)
                time.sleep(0.025)

            if joy1.get_axis(0) < -0.5:
                FL_FEMUR_ANGLE = FL_FEMUR.get_physical_angle()
                BL_FEMUR_ANGLE = BL_FEMUR.get_physical_angle()
                FL_FEMUR_MOVE = FL_FEMUR_ANGLE - 5
                BL_FEMUR_MOVE = BL_FEMUR_ANGLE - 5
                FL_FEMUR.move(FL_FEMUR_MOVE,25,False,False)
                BL_FEMUR.move(BL_FEMUR_MOVE,25,False,False)
                time.sleep(0.025)

            if joy1.get_axis(0) > 0.5:
                FR_FEMUR_ANGLE = FR_FEMUR.get_physical_angle()
                BR_FEMUR_ANGLE = BR_FEMUR.get_physical_angle()
                FL_FEMUR.move(5,50,True,False)
                BL_FEMUR.move(5,50,True,False)
                time.sleep(0.07)

            if joy1.get_axis(3) > 0.8:
                FR_HIP_ANGLE = FR_HIP.get_physical_angle()
                BR_HIP_ANGLE = BR_HIP.get_physical_angle()
                BL_HIP_MOVE = BL_HIP_ANGLE - 5
                print("HIP MOVEMENT UP")
                # FL_HIP.move(5,50,True,False)
                # BL_HIP.move(BL_HIP_MOVE,50,False,False)
                time.sleep(0.07)

            if joy1.get_axis(3) < -0.8:
                FL_HIP_ANGLE = FL_HIP.get_physical_angle()
                BL_HIP_ANGLE = BL_HIP.get_physical_angle()
                FL_HIP_MOVE = FL_HIP_ANGLE - 5
                print("HIP MOVEMENT DOWN")
                # FL_HIP.move(FL_HIP_MOVE,25,False,False)
                # BL_HIP.move(5,50,True,False)
                time.sleep(0.025)

            if joy1.get_button(1) > 0.5:

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
            
            if joy1.get_button(3) > 0.5:
                
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

            t = joy1.get_button(0)

        finally:
            if t == 1:
                print("STOP")

    
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()