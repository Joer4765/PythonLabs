from math import *

x = int(input('Enter x: '))
total = 0
for i in range(1, 41):
    total += i ** 2 * e ** -sqrt(3 * i - x)
print(f'sum = {total}')

# print((lambda x: sum(i ** 2 * e ** -(3 * i - x) ** 0.5 for i in range(1, 41)))(int(input('Enter x: '))))

