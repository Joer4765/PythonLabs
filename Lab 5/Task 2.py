import random

n = int(input("Enter n: "))
arr = [random.randint(-9, 9) for _ in range(n)]
print(*arr)

max_val = max(arr)
max_index = arr.index(max_val)
print(f"max = {max_val}\nmax index = {max_index}")

min_val = min(arr)
min_index = arr.index(min_val)
print(f"min = {min_val}\nmin index = {min_index}")

start_index, end_index = sorted([min_index, max_index])
sum_val = sum(arr[start_index:end_index + 1])
print(f"sum = {sum_val}")
