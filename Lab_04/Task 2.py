from math import acos, sqrt, fabs, pi


def get_vector_angle(coord_x1, coord_y1, coord_x2, coord_y2):
    return acos((coord_x1 * coord_x2 + coord_y1 * coord_y2) /
                (sqrt(fabs(coord_x1 * coord_x1 + coord_y1 * coord_y1)) *
                 sqrt(fabs(coord_x2 * coord_x2 + coord_y2 * coord_y2)))) * 180 / pi


x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
x3 = float(input("Enter x3: "))
y3 = float(input("Enter y3: "))

angle1 = get_vector_angle(x2 - x1, y2 - y1, x3 - x1, y3 - y1)
angle2 = get_vector_angle(x3 - x2, y3 - y2, x1 - x2, y1 - y2)
angle3 = get_vector_angle(x2 - x3, y2 - y3, x1 - x3, y1 - y3)
angle_max = max(angle3, max(angle1, angle2))

print(f"Max angle = {angle_max}")

if angle_max > 90:
    print("Obtuse")
elif angle_max < 90:
    print("Acute")
else:
    print("Right")
