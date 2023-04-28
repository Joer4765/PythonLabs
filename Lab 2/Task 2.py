from math import sqrt, pow

r, x, y = (int(input(f"Enter {i}: ")) for i in ('r', 'x', 'y'))

if x < 0:
    # (x – a) ^ 2 + (y – b) ^ 2 = r ^ 2, a = 0, b = r — circle formula
    a, b = -r, r
    dot, circle = (x - a) ** 2 + (y - b) ** 2, r ** 2

    if dot < circle:
        print('Yes')
    elif dot > circle:
        print('No')
    else:
        print('On the edge')

elif x > 0:
    if x < 2 * r and 0 < y < -r:
        print('Yes')
    elif x > 2 * r or y > 0 or y < -r:
        print('No')
    else:
        print('On the edge')

else:
    if -r < y < 0 or y == r:
        print('On the edge')
    else:
        print('No')
