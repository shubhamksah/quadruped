from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

try:

    kit.servo[0].angle = 90
    kit.servo[1].angle = 92 + 45
    kit.servo[2].angle = 100
    kit.servo[3].angle = 84
    kit.servo[4].angle = 87 - 45
    kit.servo[5].angle = 88
    kit.servo[6].angle = 90
    kit.servo[7].angle = 86 + 45
    kit.servo[8].angle = 95
    kit.servo[9].angle = 94
    kit.servo[10].angle = 86 - 45
    kit.servo[11].angle = 95 

except:
    print("Exit")
    quit()