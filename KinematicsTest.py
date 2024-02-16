from pylx16a.lx16a import *
import time
import algorithm

LX16A.initialize("/dev/ttyUSB0", 0.1)

movetime = 1000
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

    FL_TIBIA.move(164,movetime,False,False)
    FL_FEMUR.move(181.6,movetime,False,False)
    FL_HIP.move(121.5,movetime,False,False)
    FR_TIBIA.move(127,movetime,False,False)
    FR_FEMUR.move(68,movetime,False,False)
    FR_HIP.move(124,movetime,False,False)
    BR_TIBIA.move(76.5,movetime,False,False)
    BR_FEMUR.move(113.4,movetime,False,False)
    BR_HIP.move(115,movetime,False,False)
    BL_TIBIA.move(129,movetime,False,False)
    BL_FEMUR.move(173,movetime,False,False)
    BL_HIP.move(141,movetime,False,False)

    time.sleep(3)

    FL_TIBIA.move(125,movetime,False,False)
    FL_FEMUR.move(190,movetime,False,False)
    FL_HIP.move(121.5,movetime,False,False)
    FR_TIBIA.move(103,movetime,False,False)
    FR_FEMUR.move(124,movetime,False,False)
    FR_HIP.move(124,movetime,False,False)
    BR_TIBIA.move(116,movetime,False,False)
    BR_FEMUR.move(105,movetime,False,False)
    BR_HIP.move(115,movetime,False,False)
    BL_TIBIA.move(153,movetime,False,False)
    BL_FEMUR.move(117,movetime,False,False)
    BL_HIP.move(141,movetime,False,False)

    time.sleep(3)

    FL_TIBIA.move(125,movetime,False,False)
    FL_FEMUR.move(190,movetime,False,False)
    FL_HIP.move(121.5,movetime,False,False)
    FR_TIBIA.move(92,movetime,False,False)
    FR_FEMUR.move(69,movetime,False,False)
    FR_HIP.move(124,movetime,False,False)
    BR_TIBIA.move(116,movetime,False,False)
    BR_FEMUR.move(105,movetime,False,False)
    BR_HIP.move(115,movetime,False,False)
    BL_TIBIA.move(164,movetime,False,False)
    BL_FEMUR.move(172,movetime,False,False)
    BL_HIP.move(141,movetime,False,False)

    # time.sleep(3)

    # FL_TIBIA.move(149,movetime,False,False)
    # FL_FEMUR.move(134,movetime,False,False)
    # FL_HIP.move(121.5,movetime,False,False)
    # FR_TIBIA.move(110,movetime,False,False)
    # FR_FEMUR.move(115,movetime,False,False)
    # FR_HIP.move(124,movetime,False,False)
    # BR_TIBIA.move(92,movetime,False,False)
    # BR_FEMUR.move(161,movetime,False,False)
    # BR_HIP.move(115,movetime,False,False)
    # BL_TIBIA.move(146,movetime,False,False)
    # BL_FEMUR.move(126,movetime,False,False)
    # BL_HIP.move(141,movetime,False,False)

    # time.sleep(3)

    # FL_TIBIA.move(164,movetime,False,False)
    # FL_FEMUR.move(181.6,movetime,False,False)
    # FL_HIP.move(121.5,movetime,False,False)
    # FR_TIBIA.move(110,movetime,False,False)
    # FR_FEMUR.move(115,movetime,False,False)
    # FR_HIP.move(124,movetime,False,False)
    # BR_TIBIA.move(76.5,movetime,False,False)
    # BR_FEMUR.move(113.4,movetime,False,False)
    # BR_HIP.move(115,movetime,False,False)
    # BL_TIBIA.move(146,movetime,False,False)
    # BL_FEMUR.move(126,movetime,False,False)
    # BL_HIP.move(141,movetime,False,False)




except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()
 