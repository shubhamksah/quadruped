import time
import pygame
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
angle = 90

def standing_position(FL_TIBIA,FL_FEMUR,FL_HIP,FR_TIBIA,FR_FEMUR,FR_HIP,BR_TIBIA,BR_FEMUR,BR_HIP,BL_TIBIA,BL_FEMUR,BL_HIP):

    kit.servo[1].angle = angle
    kit.servo[2].angle = angle
    kit.servo[3].angle = 85
    kit.servo[4].angle = angle
    kit.servo[5].angle = angle
    kit.servo[6].angle = 90
    kit.servo[7].angle = angle
    kit.servo[8].angle = angle
    kit.servo[9].angle = 95
    kit.servo[10].angle = angle
    kit.servo[11].angle = angle
    kit.servo[12].angle = 90        
    


t = 0