import algorithm

x = 114
y = 70

ik_algorithm = algorithm.inverse_kinematics_2dof(x,y)

print(ik_algorithm)

Femur_angle = ik_algorithm [0]

print(Femur_angle)

Tibia_angle = ik_algorithm [1]

print(Tibia_angle)
