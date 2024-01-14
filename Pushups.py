from math import sin, cos
from pylx16a.lx16a import *
import time
import servoresetmodule

LX16A.initialize("/dev/ttyUSB0", 0.1)

servo1 = LX16A(1)
servo2 = LX16A(2)
servo3 = LX16A(3)
servo4 = LX16A(4)
servo5 = LX16A(5)
servo6 = LX16A(6)
servo7 = LX16A(7)
servo8 = LX16A(8)
servo9 = LX16A(9)
servo10 = LX16A(10)
servo11 = LX16A(11)
servo12 = LX16A(12)

servoresetmodule.resetservo(servo1,servo2,servo3,servo4,servo5,servo6,servo7,servo8,servo9,servo10,servo11,servo12)

servo1angle = servo1.get_physical_angle()
servo2angle = servo2.get_physical_angle()
servo3angle = servo3.get_physical_angle()
servo4angle = servo4.get_physical_angle()
servo5angle = servo5.get_physical_angle()
servo6angle = servo6.get_physical_angle()
servo7angle = servo7.get_physical_angle()
servo8angle = servo8.get_physical_angle()
servo9angle = servo9.get_physical_angle()
servo10angle = servo10.get_physical_angle()
servo11angle = servo11.get_physical_angle()
servo12angle = servo12.get_physical_angle()

increment45 = 45
increment20 = 20
increment10 = 10

times = 0

movetime = 1000
try:
    while times != 7:

        time.sleep(1)

        servoresetmodule.resetservo(servo1,servo2,servo3,servo4,servo5,servo6,servo7,servo8,servo9,servo10,servo11,servo12)

        time.sleep(1)

        servo1angle = servo1.get_physical_angle()
        servo2angle = servo2.get_physical_angle()
        servo3angle = servo3.get_physical_angle()
        servo4angle = servo4.get_physical_angle()
        servo5angle = servo5.get_physical_angle()
        servo6angle = servo6.get_physical_angle()
        servo7angle = servo7.get_physical_angle()
        servo8angle = servo8.get_physical_angle()
        servo9angle = servo9.get_physical_angle()
        servo10angle = servo10.get_physical_angle()
        servo11angle = servo11.get_physical_angle()
        servo12angle = servo12.get_physical_angle()

        servo2angle += increment45
        servo5angle -= increment45
        servo8angle -= increment45
        servo11angle += increment45

        servo2.move(servo2angle,movetime,False,False)
        servo5.move(servo5angle,movetime,False,False)
        servo8.move(servo8angle,movetime,False,False)
        servo11.move(servo11angle,movetime,False,False)

        time.sleep(1)

        servoresetmodule.resetservo(servo1,servo2,servo3,servo4,servo5,servo6,servo7,servo8,servo9,servo10,servo11,servo12)

        time.sleep(1)

        servo1angle = servo1.get_physical_angle()
        print("servo1angle: ", servo1angle )
        servo2angle = servo2.get_physical_angle()
        print("servo2angle: ", servo2angle )
        servo3angle = servo3.get_physical_angle()
        print("servo3angle: ", servo3angle )
        servo4angle = servo4.get_physical_angle()
        print("servo4angle: ", servo4angle )
        servo5angle = servo5.get_physical_angle()
        print("servo5angle: ", servo5angle )
        servo6angle = servo6.get_physical_angle()
        print("servo6angle: ", servo6angle )
        servo7angle = servo7.get_physical_angle()
        print("servo7angle: ", servo7angle )
        servo8angle = servo8.get_physical_angle()
        print("servo8angle: ", servo8angle )
        servo9angle = servo9.get_physical_angle()
        print("servo9angle: ", servo9angle )
        servo10angle = servo10.get_physical_angle()
        print("servo10angle: ", servo10angle )
        servo11angle = servo11.get_physical_angle()
        print("servo11angle: ", servo11angle )
        servo12angle = servo12.get_physical_angle()
        print("servo12angle: ", servo12angle )

        times += 1
except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()
