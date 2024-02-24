from pylx16a.lx16a import *
import time
import algorithm

LX16A.initialize("/dev/ttyUSB0", 0.1)

movetime = 300
timesleep = 2
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
    
    FL_TIBIA.move(135,movetime,False,False)
    FL_FEMUR.move(134,movetime,False,False)
    FL_HIP.move(121.5,movetime,False,False)
    FR_TIBIA.move(112,movetime,False,False)
    FR_FEMUR.move(124,movetime,False,False)
    FR_HIP.move(124,movetime,False,False)
    BR_TIBIA.move(106,movetime,False,False)
    BR_FEMUR.move(161,movetime,False,False)
    BR_HIP.move(115,movetime,False,False)
    BL_TIBIA.move(144,movetime,False,False)
    BL_FEMUR.move(117,movetime,False,False)
    BL_HIP.move(141,movetime,False,False)

    time.sleep(timesleep)

    FL_TIBIA.move(135,movetime,False,False)
    FL_FEMUR.move(134,movetime,False,False)
    FL_HIP.move(121.5,movetime,False,False)
    FR_TIBIA.move(92,1000,False,False)
    FR_FEMUR.move(69,1000,False,False)
    FR_HIP.move(124,1000,False,False)
    BR_TIBIA.move(106,movetime,False,False)
    BR_FEMUR.move(161,movetime,False,False)
    BR_HIP.move(115,movetime,False,False)
    BL_TIBIA.move(164,1000,False,False)
    BL_FEMUR.move(172,1000,False,False)
    BL_HIP.move(141,1000,False,False)



except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()
 