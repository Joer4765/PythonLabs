import random

n = int(input('Enter n: '))
matrix = [[random.randrange(-50, 50) for j in range(n)] for i in range(n)]

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]), end='\n\n')
uniques = [i for i in range(n) if len(matrix[i]) == len(set(matrix[i]))]
print(* uniques if uniques else ['There is no rows with unique elements'])
