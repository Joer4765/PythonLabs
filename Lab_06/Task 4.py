n = int(input('n: '))
arr = []
print('Matrix:')
matrix = [list(map(int, input().split())) for _ in range(n)]
print('Last even index elements:')
for i in range(n):
    length = len(matrix[i]) - 1
    arr.append(matrix[i][length - length % 2])
    print(arr[i], end=' ')
