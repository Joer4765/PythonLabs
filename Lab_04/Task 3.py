from math import pow


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def b(n):
    if n == 1:
        return 1
    return pow(a(n - 1), 2) + pow(b(n - 1), 2)


def a(n):
    if n == 1:
        return 1
    return 0.3 * b(n - 1) + 0.2 * a(n - 1)


def sum(n):
    if n == 1:
        return 0.5
    return a(n) * b(n) / factorial(n + 1) + sum(n - 1)


n = int(input("Enter n: "))
print(sum(n))
