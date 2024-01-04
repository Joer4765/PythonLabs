x, y, z, k = (int(input(f"Enter {i}: ")) for i in ('x', 'y', 'z', 'k'))

if k == 1:
    print(min(max(x, y), z))
elif 5 <= k <= 10:
    print(min(max(y, z), x))
elif 15 <= k <= 20:
    print(min(max(z, x), y))
else:
    print(x + y + z)
