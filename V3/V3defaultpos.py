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

    pos1move = 0.75
    pos2move = 1.75
    while pos2move <= 7:
        kit.servo[1].angle = FLF + pos1move
        kit.servo[10].angle = BRF - pos1move
        pos1move += 0.75
        kit.servo[0].angle = FLT + pos2move
        kit.servo[9].angle = BRT - pos2move
        pos2move += 1.75
        time.sleep(0.0025)

    time.sleep(0.5)


    pos1move = 1.5625
    pos2move = 3
    while pos2move <= 48:
        kit.servo[1].angle = FLF + pos1move
        kit.servo[10].angle = BRF - pos1move
        pos1move += 1.5625
        kit.servo[0].angle = FLT + pos2move
        kit.servo[9].angle = BRT - pos2move
        pos2move += 3
        time.sleep(0.0025)

except:
    print("Exit")
    quit()