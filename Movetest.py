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

increment40 = 40
increment20 = 20

try:

    movetime = 1000

    servo1angle -= increment40
    servo4angle += increment40
    servo7angle += increment40
    servo10angle -= increment40

    servo1.move(servo1angle,movetime,False,False)
    servo4.move(servo4angle,movetime,False,False)
    servo7.move(servo7angle,movetime,False,False)
    servo10.move(servo10angle,movetime,False,False)

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

    servo1angle += increment40
    servo4angle -= increment40
    servo7angle -= increment40
    servo10angle += increment40

    time.sleep(1)

    servo1.move(servo1angle,movetime,False,False)
    servo4.move(servo4angle,movetime,False,False)
    servo7.move(servo7angle,movetime,False,False)
    servo10.move(servo10angle,movetime,False,False) 

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

    servo3angle -= increment20
    servo6angle -= increment20
    servo9angle += increment20
    servo12angle += increment20

    servo3.move(servo3angle,movetime,False,False)
    servo6.move(servo6angle,movetime,False,False)
    servo9.move(servo9angle,movetime,False,False)
    servo12.move(servo12angle,movetime,False,False)

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

    servo3angle += increment20
    servo6angle += increment20
    servo9angle -= increment20
    servo12angle -= increment20

    servo3.move(servo3angle,movetime,False,False)
    servo6.move(servo6angle,movetime,False,False)
    servo9.move(servo9angle,movetime,False,False)
    servo12.move(servo12angle,movetime,False,False)

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

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()
