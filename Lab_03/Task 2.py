from math import pow

limit = int(input("Enter limit for k: "))
overflow = False
total = 0

for x in range(1, 6):
    for k in range(1, limit+1):
        add = pow(-1, k) * pow(x, 2*k) / (x * (k+1) * (k+2))
        if total + add == float('inf'):
            print(f"Reached double type limit at k = {k}")
            overflow = True
            break
        total += add
    if overflow:
        break

print(f"sum = {total}")