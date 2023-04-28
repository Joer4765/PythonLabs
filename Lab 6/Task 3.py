from random import randrange

m = 12
stores = int(input('Stores: '))
incomes = [[randrange(0, 100) for _ in range(m)] for _ in range(stores)]
print(' ' * 5, 'Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4', sep=' ' * 6)
for i in range(stores):
    print(f'Store {i}: ', end='')
    for j in range(m):
        print(f'{incomes[i][j]:{[4, 7][j % 3 == 0 and j > 0]}}', end='')
    print()
store, quarter = int(input('\nStore: ')), int(input('Quarter: '))
res_incomes = incomes[store][(quarter - 1) * 3:quarter * 3]
print(f'Incomes:', *res_incomes)
print(f'Total income:', sum(res_incomes))
