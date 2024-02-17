import math

try:

    x = 80
    y = 130

    q1 = 70
    q2 = 114

    A = math.sqrt((math.pow(x,2)+math.pow(y,2)))

    alpha2 = math.acos((math.pow(q1,2)+math.pow(q2,2)-math.pow(A,2))/(2*q1*q2))

    theta2 = math.pi-alpha2

    alpha4 = math.atan(x/y)

    q3 = math.cos(theta2)*q2
    alpha1 = math.acos((q1+q3)/A)

    theta1 = alpha4-alpha1

    Tibia_angle = math.degrees(theta2)
    Femur_angle = math.degrees(theta1)

    print("TIBIA: ", Tibia_angle)
    print("FEMUR: ", Femur_angle)

    TIBIA = (45 - Tibia_angle - Femur_angle)
    FEMUR = Femur_angle

    print("tibia: ", TIBIA)
    print("femur: ", FEMUR)

except:
    print("STOP")
