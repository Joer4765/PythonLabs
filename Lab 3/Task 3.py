from math import pow, isinf, factorial, fabs

x = float(input("Enter x: "))
e = float(input("Enter e: "))

total = 0.0
i = 0

while True:
    i += 1
    factorial_i = factorial(2*i)
    add = pow(-1, i-1) * pow(x, 2*i) / factorial_i
    if isinf(total + add) or fabs(add) < e * fabs(total):
        break
    total += add

print(f"sum = {total}\nAdditions = {i}")