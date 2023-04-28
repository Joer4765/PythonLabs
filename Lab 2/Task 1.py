from math import sqrt, pow

x, r = int(input("Enter x: ")), int(input('Enter r: '))

if x < -r:
    print(f"y = {r}")
elif x < r:
    #  (x – a)^2 + (y – b)^2 = r^2, a = 0, b = r — circle formula
    #  x^2 + (y - r)^2 = r^2
    #  (y - r)^2 = r^2 - x^2
    #  Abs(y - r) = Sqrt(r^2 - x^2)
    #  y = r + Sqrt(r^2 - x^2)
    #  y = r - Sqrt(r^2 - x^2) — we need this
    print(f"y = {r - sqrt(pow(r, 2) - pow(x, 2))}")
elif x < 2 * r:
    #  (x - x1) / (x2 - x1) = (y - y1 / y2 - y1) — formula of a line passing through two points
    #  y - y1 =  (x - x1) * (y2 - y1) / (x2 - x1)
    #  y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)
    y1 = r
    y2 = -r
    x1 = r
    x2 = 2 * r
    print(f"y = {y1 + (x - x1) * (y2 - y1) / (x2 - x1)}")
else:
    #  y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)
    y1 = -r
    y2 = 0
    x1 = 2 * r
    x2 = 3 * r
    print(f"y = {y1 + (x - x1) * (y2 - y1) / (x2 - x1)}")


