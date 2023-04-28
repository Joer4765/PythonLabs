import math

r = 3
n = 3
hits = [False] * 10
coordinates = [""] * 10

for i in range(n):
    x = float(input(f"Enter x{i + 1}: "))
    y = float(input(f"Enter y{i + 1}: "))
    hit = (math.pow(x + r, 2) + math.pow(y - r, 2) <= math.pow(r, 2)) or (x <= 2 * r and -r <= y <= 0)
    hits[i] = hit
    coordinates[i] = f"{x} {y}"
    print()

print(f'{"Number":<8}{"Coords":<10}{"Result":<10}')
for i in range(n):
    print(f'{i + 1:<8}{coordinates[i]:<10}{("Yes" if hits[i] else "No"):<10}')
