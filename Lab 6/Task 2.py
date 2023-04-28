import numpy as np
from random import randrange

n, m = int(input('Enter n: ')), int(input('Enter m: '))

A = np.array([[randrange(-50, 50) for _ in range(m)] for _ in range(n)])
totals = [sum(A[:, i]) for i in range(m)]
print(A, f'min sum: {min(totals)}', f'Index: {totals.index(min(totals))}', sep='\n')
