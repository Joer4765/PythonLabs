def func(input_array) -> list:
    n = len(input_array)
    result = []

    for i in range(n):
        total = 0
        for j in range(len(input_array[i])):
            if input_array[i][j] >= 0:
                continue
            total += input_array[i][j]
        result.append(total)

    return result
