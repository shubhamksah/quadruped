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

    kit.servo[0].angle = 88
    kit.servo[1].angle = 137
    kit.servo[2].angle = 100
    kit.servo[3].angle = 84
    kit.servo[4].angle = 42
    kit.servo[5].angle = 88
    kit.servo[6].angle = 100
    kit.servo[7].angle = 131
    kit.servo[8].angle = 95
    kit.servo[9].angle = 93
    kit.servo[10].angle = 41
    kit.servo[11].angle = 95 

    pos1move = 1.5625
    pos2move = 3
    while pos2move <= 48:
        kit.servo[1].angle = FLF + pos1move
        kit.servo[10].angle = BRF - pos1move
        pos1move += 1.5625
        kit.servo[0].angle = FLT + pos2move
        kit.servo[9].angle = BRT - pos2move
        pos2move += 3
        time.sleep(0.05)

except:
    print("Exit")
    quit()