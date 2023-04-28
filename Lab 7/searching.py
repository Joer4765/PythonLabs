
def linear_search(arr, search):
    for i in range(len(arr)):
        if arr[i] == search:
            return i
    return -1


def binary_search(arr, search):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2

        # Check if x is present at mid
        if arr[m] == search:
            return m

        # If x greater, ignore left half
        elif arr[m] < search:
            l = m + 1

        # If x is smaller, ignore right half
        else:
            r = m - 1
    return -1


def lcs(x, y, m, n):
    if m == 0 or n == 0:
        return 0
    if x[m - 1] == y[n - 1]:
        return 1 + lcs(x, y, m - 1, n - 1)
    else:
        return max(lcs(x, y, m, n - 1), lcs(x, y, m - 1, n))
