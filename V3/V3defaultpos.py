import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

FLT = 88
FLF = 137
FLH = 100
FRT = 84
FRF = 42
FRH = 88
BLT = 100
BLF = 131
BLH = 95
BRT = 93
BRF = 41
BRH = 95 

try:

    kit.servo[0].angle = 90
    kit.servo[1].angle = 135
    kit.servo[2].angle = 100
    kit.servo[3].angle = 97
    kit.servo[4].angle = 45
    kit.servo[5].angle = 88
    kit.servo[6].angle = 100
    kit.servo[7].angle = 130
    kit.servo[8].angle = 95
    kit.servo[9].angle = 94
    kit.servo[10].angle = 45
    kit.servo[11].angle = 95   

except:
    print("Exit")
    quit()