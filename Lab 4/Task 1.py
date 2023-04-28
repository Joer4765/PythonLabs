from math import pow, sqrt


def triangle_square(diagonal):
    return pow(diagonal, 2) / 2


def triangle_perimeter(diagonal):
    return 2 * diagonal * sqrt(2)


d = float(input("Enter diagonal: "))
print(f"Square = {triangle_square(d)}")
print(f"Perimeter = {triangle_perimeter(d)}")
