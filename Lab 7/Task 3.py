import tkinter as tk
from tkinter import ttk
from searching import *
from help_funcs import *
from random import randrange, choice

arr = [randrange(-24, 25) for _ in range(50)]
arr_sorted = sorted(arr)
A = [randrange(-24, 25) for _ in range(10)]
B = [randrange(-24, 25) for _ in range(10)]
search = choice(arr)

root = tk.Tk()

label = ttk.Label(root, text='arr: ')
label.pack()

text = tk.Text(root, width=50, height=4, padx=10, wrap='char')
text.pack()
text.insert('1.0', arr2text(arr))
text['state'] = 'disabled'

label = ttk.Label(root, text='arr_sorted: ')
label.pack()

text = tk.Text(root, width=50, height=4, padx=10, wrap='char')
text.pack()
text.insert('1.0', arr2text(arr_sorted))
text['state'] = 'disabled'

label = ttk.Label(root, text='find: ')
label.pack()

text = tk.Text(root, width=50, height=1, padx=10, wrap='char')
text.pack()
text.insert('1.0', str(search))
text['state'] = 'disabled'

label = ttk.Label(root, text='A: ')
label.pack()

text = tk.Text(root, width=50, height=1, padx=10, wrap='char')
text.pack()
text.insert('1.0', arr2text(A))
text['state'] = 'disabled'

label = ttk.Label(root, text='B: ')
label.pack()

text = tk.Text(root, width=50, height=1, padx=10, wrap='char')
text.pack()
text.insert('1.0', arr2text(B))
text['state'] = 'disabled'

label = ttk.Label(root, text='linear_search: ')
label.pack()

text = tk.Text(root, width=50, height=1, padx=10, wrap='char')
text.pack()
text.insert('1.0', str(linear_search(arr, search)))
text['state'] = 'disabled'

label = ttk.Label(root, text='binary_search: ')
label.pack()

text = tk.Text(root, width=50, height=1, padx=10, wrap='char')
text.pack()
text.insert('1.0', str(binary_search(arr_sorted, search)))
text['state'] = 'disabled'

label = ttk.Label(root, text='lcs: ')
label.pack()

text = tk.Text(root, width=50, height=1, padx=10, wrap='char')
text.pack()
text.insert('1.0', str(lcs(A, B, len(A), len(B))))
text['state'] = 'disabled'

root.mainloop()
