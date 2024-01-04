from random import Random

n = int(input("Enter n: "))
array = [0] * n
array2 = [0.0] * n
rand = Random()
total = 0

print("Input massive: ")
for i in range(n):
    array[i] = rand.randint(-9, 10)
    print(f"{array[i]} ", end='')
    total += array[i]
print()

avg = total / n
print(f"{avg = }")
print("Output massive: ")
for i in range(n):
    array2[i] = round(array[i] - avg, 2)
    print(f"{array2[i]} ", end='')
