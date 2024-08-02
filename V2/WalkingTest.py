from pylx16a.lx16a import *
import time
import algorithm

LX16A.initialize("/dev/ttyUSB0", 0.1)

movetime = 300
movetime2 = 300
timesleep = 0.3
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

    a=1
    while (a < 10) :
        FL_TIBIA.move(130,movetime,False,False) #FL UP
        FL_FEMUR.move(134,movetime,False,False) #FL UP
        FL_HIP.move(121.5,movetime,False,False)
        FR_TIBIA.move(103,movetime2,False,False) #FR DOWN
        FR_FEMUR.move(124,movetime2,False,False) #FR DOWN
        FR_HIP.move(124,movetime,False,False)
        BR_TIBIA.move(111,movetime,False,False) #BR UP
        BR_FEMUR.move(161,movetime,False,False) #BR UP
        BR_HIP.move(115,movetime,False,False)
        BL_TIBIA.move(153,movetime2,False,False) #BL Down
        BL_FEMUR.move(117,movetime2,False,False) #BL Down
        BL_HIP.move(141,movetime,False,False)

        time.sleep(timesleep)

        FL_TIBIA.move(130,movetime,False,False) #FL UP
        FL_FEMUR.move(134,movetime,False,False) #FL UP
        FL_HIP.move(121.5,movetime,False,False)
        FR_TIBIA.move(77,movetime2,False,False) #FR BACK
        FR_FEMUR.move(89,movetime2,False,False) #FR BACK
        FR_HIP.move(124,movetime,False,False)
        BR_TIBIA.move(111,movetime,False,False) #BR UP
        BR_FEMUR.move(161,movetime,False,False) #BR UP
        BR_HIP.move(115,movetime,False,False)
        BL_TIBIA.move(179,movetime2,False,False) #BL BACK
        BL_FEMUR.move(152,movetime2,False,False) #BL BACK
        BL_HIP.move(141,movetime,False,False)

        time.sleep(timesleep)

        FL_TIBIA.move(149,movetime2,False,False) #FL DOWN
        FL_FEMUR.move(134,movetime2,False,False) #FL DOWN
        FL_HIP.move(121.5,movetime,False,False)
        FR_TIBIA.move(123,movetime,False,False) #FR UP
        FR_FEMUR.move(124,movetime,False,False) #FR UP
        FR_HIP.move(124,movetime,False,False)
        BR_TIBIA.move(92,movetime2,False,False) #BR DOWN
        BR_FEMUR.move(161,movetime2,False,False) #BR DOWN
        BR_HIP.move(115,movetime,False,False)
        BL_TIBIA.move(134,movetime,False,False) #BL UP
        BL_FEMUR.move(117,movetime,False,False) #BL UP
        BL_HIP.move(141,movetime,False,False)

        time.sleep(timesleep)

        FL_TIBIA.move(175,movetime2,False,False) #FL BACK
        FL_FEMUR.move(169,movetime2,False,False) #FL BACK
        FL_HIP.move(121.5,movetime,False,False)
        FR_TIBIA.move(123,movetime,False,False) #FR UP
        FR_FEMUR.move(124,movetime,False,False) #FR UP
        FR_HIP.move(124,movetime,False,False)
        BR_TIBIA.move(66,movetime2,False,False) #BR BACK
        BR_FEMUR.move(126,movetime2,False,False) #BR BACK
        BR_HIP.move(115,movetime,False,False)
        BL_TIBIA.move(134,movetime,False,False) #BL UP
        BL_FEMUR.move(117,movetime,False,False) #BL UP
        BL_HIP.move(141,movetime,False,False)

        time.sleep(timesleep)

        if( a == 4):
            break      

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()
 