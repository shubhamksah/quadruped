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


try:
    servo1.move()

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()
