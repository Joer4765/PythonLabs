import math
import random

n = int(input('Enter n: '))
x = [round(random.uniform(0, 10), 2) for _ in range(n)]
y = []
r = [0] * (n + n % 2)

for i in range(n):
    if math.cos(x[i]) > 0:
        y.append(x[i] ** 3 - 7.5)
    else:
        y.append(x[i] ** 2 - 5 * math.exp(math.sin(x[i])))
    if i % 2 == 0:
        r[i] = x[i]
        r[i + 1] = y[i]
        print(r[i], r[i + 1], end=' ')
print()
