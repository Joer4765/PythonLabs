import math


x = float(input("Enter angle in radians: ")) % math.sqrt(3)
eps = float(input("Enter e: "))

arcctg = math.pi / 2
prevSum = 0
i = 0

print(f'{"Argument":10}{"Function":10}{"Additions":10}')
while True:
    add = math.pow(-1, i + 1) * math.pow(x, 2 * i + 1) / (2 * i + 1)
    arcctg += add
    i += 1
    print(f'{x:<10.2f}{arcctg * 180 / math.pi:<10.2f}{i:<10d}')
    if abs(add) <= eps * abs(arcctg):
        break

print(f'Taylor: {arcctg * 180 / math.pi}')
print(f'Function: {math.atan(1 / x) * 180 / math.pi}')
