from pylx16a.lx16a import *
import time

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

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()