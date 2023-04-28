import math


def bubble_sort(arr):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for j in range(len(arr) - 1):
            if arr[j] <= arr[j + 1]:
                continue
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            is_sorted = False
    return arr


def shaker_sort(arr):
    is_sorted = False
    shaker = 0
    while not is_sorted:
        is_sorted = True
        for i in range(shaker, len(arr) - shaker - 1):
            if arr[i] <= arr[i + 1]:
                continue
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            is_sorted = False
        for i in range(len(arr) - shaker - 1, shaker, -1):
            if arr[i] >= arr[i - 1]:
                continue
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            is_sorted = False
        shaker += 1
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] >= arr[j - 1]:
                break
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


def stooge_sort(arr):
    def func(arr, l, h):
        if l >= h:
            return
        if arr[l] > arr[h]:
            arr[l], arr[h] = arr[h], arr[l]
        if h - l + 1 > 2:
            t = math.floor((h - l + 1) / 3)
            func(arr, l, h - t)
            func(arr, l + t, h)
            func(arr, l, h - t)

    func(arr, 0, len(arr) - 1)

    return arr


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and arr[j] < arr[j - gap]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap
        gap //= 2
    return arr


def merge_sort(arr):
    def merge(arr, l, m, r):
        # Find sizes of two
        # subarrays to be merged
        n1 = m - l + 1
        n2 = r - m

        # Create temp arrays
        L = [0] * n1
        R = [0] * n2
        i = 0
        j = 0

        # Copy data to temp arrays
        for i in range(n1):
            L[i] = arr[l + i]
        for j in range(n2):
            R[j] = arr[m + 1 + j]

        # Merge the temp arrays
        i = 0
        j = 0
        k = l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy remaining elements
        # of L[] if any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy remaining elements
        # of R[] if any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def sort(arr, l, r):
        if l < r:
            # Find the middle
            # point
            m = (r + l) // 2

            # Sort first and
            # second halves
            sort(arr, l, m)
            sort(arr, m + 1, r)

            # Merge the sorted halves
            merge(arr, l, m, r)

    sort(arr, 0, len(arr) - 1)
    return arr


def selection_sort(arr):
    def sort(arr):
        n = len(arr)

        # One by one move boundary of unsorted subarray
        for i in range(n - 1):
            # Find the minimum element in unsorted array
            minIdx = i
            for j in range(i + 1, n):
                if arr[j] < arr[minIdx]:
                    minIdx = j

            # Swap the found minimum element with the first element
            arr[minIdx], arr[i] = arr[i], arr[minIdx]

    sort(arr)

    return arr


def quick_sort(arr):
    def sort(arr, low, high):
        if low < high:
            # pi is partitioning index, arr[p]
            # is now at right place
            pi = partition(arr, low, high)

            # Separately sort elements before
            # and after partition index
            sort(arr, low, pi - 1)
            sort(arr, pi + 1, high)

    def partition(arr, low, high):
        # Choosing the pivot
        pivot = arr[high]

        # Index of smaller element and indicates
        # the right position of pivot found so far
        i = low - 1

        for j in range(low, high):
            # If current element is smaller than the pivot
            if arr[j] < pivot:
                # Increment index of smaller element
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    sort(arr, 0, len(arr) - 1)
    return arr
