from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

try:

    kit.servo[0].angle = 50
    kit.servo[1].angle = 150
    kit.servo[2].angle = 100
    kit.servo[3].angle = 137
    kit.servo[4].angle = 30
    kit.servo[5].angle = 88
    kit.servo[6].angle = 48
    kit.servo[7].angle = 145
    kit.servo[8].angle = 95
    kit.servo[9].angle = 134
    kit.servo[10].angle = 30
    kit.servo[11].angle = 95  

except:
    print("Exit")
    quit()