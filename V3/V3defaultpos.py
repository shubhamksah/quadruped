from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

try:

    kit.servo[1].angle = 90
    kit.servo[2].angle = 90
    kit.servo[3].angle = 114
    kit.servo[4].angle = 90
    kit.servo[5].angle = 90
    kit.servo[6].angle = 110
    kit.servo[7].angle = 90
    kit.servo[8].angle = 90
    kit.servo[9].angle = 100
    kit.servo[10].angle = 90
    kit.servo[11].angle = 90
    kit.servo[12].angle = 90  

except:
    print("Exit")
    quit()