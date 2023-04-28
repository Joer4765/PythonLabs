from math import pow

weight = float(input("Enter grain weight: "))

total = 0
print("1 grain for 1 cell")
for i in range(64):
    grains = pow(2, i)
    total += grains
    print(f"{grains:,.0f} grains for {i+1} cells")

print()
print(f"{total:,.0f} - grains total count")
print(f"{total * weight:,.0f} - grains total weight")

