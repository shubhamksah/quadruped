from pylx16a.lx16a import *
import time

def standing_position(FL_TIBIA,FL_FEMUR,FL_HIP,FR_TIBIA,FR_FEMUR,FR_HIP,BR_TIBIA,BR_FEMUR,BR_HIP,BL_TIBIA,BL_FEMUR,BL_HIP):

    FL_TIBIA.move(125,1000,False,False)
    FL_FEMUR.move(143,1000,False,False)
    FL_HIP.move(121.5,1000,False,False)
    FR_TIBIA.move(120,1000,False,False)
    FR_FEMUR.move(115,1000,False,False)
    FR_HIP.move(124,1000,False,False)
    BR_TIBIA.move(120,1000,False,False)
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

    resting_position(FL_TIBIA,FL_FEMUR,FL_HIP,FR_TIBIA,FR_FEMUR,FR_HIP,BR_TIBIA,BR_FEMUR,BR_HIP,BL_TIBIA,BL_FEMUR,BL_HIP)

    time.sleep(2000)

    standing_position(FL_TIBIA,FL_FEMUR,FL_HIP,FR_TIBIA,FR_FEMUR,FR_HIP,BR_TIBIA,BR_FEMUR,BR_HIP,BL_TIBIA,BL_FEMUR,BL_HIP)

    FL_TIBIAangle = FL_TIBIA.get_physical_angle()
    print("sevo1angle: ", FL_TIBIAangle )
    FL_FEMURangle = FL_FEMUR.get_physical_angle()
    print("sevo2angle: ", FL_FEMURangle )
    FL_HIPangle = FL_HIP.get_physical_angle()
    print("sevo3angle: ", FL_HIPangle )
    FR_TIBIAangle = FR_TIBIA.get_physical_angle()
    print("sevo4angle: ", FR_TIBIAangle )
    FR_FEMURangle = FR_FEMUR.get_physical_angle()
    print("sevo5angle: ", FR_FEMURangle )
    FR_HIPangle = FR_HIP.get_physical_angle()
    print("sevo6angle: ", FR_HIPangle )
    BR_TIBIAangle = BR_TIBIA.get_physical_angle()
    print("sevo7angle: ", BR_TIBIAangle )
    BR_FEMURangle = BR_FEMUR.get_physical_angle()
    print("sevo8angle: ", BR_FEMURangle )
    BR_HIPangle = BR_HIP.get_physical_angle()
    print("sevo9angle: ", BR_HIPangle )
    BL_TIBIAangle = BL_TIBIA.get_physical_angle()
    print("sevo10angle: ", BL_TIBIAangle )
    BL_FEMURangle = BL_FEMUR.get_physical_angle()
    print("sevo11angle: ", BL_FEMURangle )
    BL_HIPangle = BL_HIP.get_physical_angle()
    print("sevo12angle: ", BL_HIPangle )

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()