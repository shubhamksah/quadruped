from pylx16a.lx16a import *
import time
import algorithm

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

    x=84
    y=130

    angle = algorithm.inverse_kinematics_2dof(x,y)
    print(angle[0])
    print(angle[1])

    FL_FEMUR_MOVE = 143 - angle[0]
    FL_TIBIA_MOVE = 85+(80 - angle[1])

    print(FL_TIBIA_MOVE)
    print(FL_TIBIA.get_physical_angle())

    FL_FEMUR.move(FL_FEMUR_MOVE,1000,False,False)
    FL_TIBIA.move(FL_TIBIA_MOVE,1000,False,False)

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()
