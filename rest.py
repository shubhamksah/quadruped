from math import sin, cos
from pylx16a.lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0", 0.1)

increment40 = 40
increment20 = 20
increment10 = 10

movetime = 1000

try:

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

    servo1.move(85.52,1000,False,False)
    servo2.move(169.92,1000,False,False)
    servo3.move(121.92,1000,False,False)
    servo4.move(161.44,1000,False,False)
    servo5.move(84.72,1000,False,False)
    servo6.move(124.08,1000,False,False)
    servo7.move(154.24,1000,False,False)
    servo8.move(122.4,1000,False,False)
    servo9.move(110.88,1000,False,False)
    servo10.move(91.52,1000,False,False)
    servo11.move(153.12,1000,False,False)
    servo12.move(141.84,1000,False,False)

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

    servo1angle = servo1.get_physical_angle()
    print("sevo1angle: ", servo1angle )
    servo2angle = servo2.get_physical_angle()
    print("sevo2angle: ", servo2angle )
    servo3angle = servo3.get_physical_angle()
    print("sevo3angle: ", servo3angle )
    servo4angle = servo4.get_physical_angle()
    print("sevo4angle: ", servo4angle )
    servo5angle = servo5.get_physical_angle()
    print("sevo5angle: ", servo5angle )
    servo6angle = servo6.get_physical_angle()
    print("sevo6angle: ", servo6angle )
    servo7angle = servo7.get_physical_angle()
    print("sevo7angle: ", servo7angle )
    servo8angle = servo8.get_physical_angle()
    print("sevo8angle: ", servo8angle )
    servo9angle = servo9.get_physical_angle()
    print("sevo9angle: ", servo9angle )
    servo10angle = servo10.get_physical_angle()
    print("sevo10angle: ", servo10angle )
    servo11angle = servo11.get_physical_angle()
    print("sevo11angle: ", servo11angle )
    servo12angle = servo12.get_physical_angle()
    print("sevo12angle: ", servo12angle )

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()