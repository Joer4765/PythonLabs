import tkinter as tk
from tkinter import ttk
from sorting import *
from help_funcs import *
from random import randrange

arr = [randrange(-24, 25) for _ in range(50)]

root = tk.Tk()

input_label = ttk.Label(root, text='input_array: ')
input_label.pack()

input_text = tk.Text(root, width=50, height=4, padx=10, wrap='char')
input_text.pack()
input_text.insert('1.0', arr2text(arr))
input_text['state'] = 'disabled'


def call(output_text, func):
    output(output_text, arr2text(func(arr.copy())))


text = []
for func in [bubble_sort, shaker_sort, insertion_sort, stooge_sort, shell_sort, merge_sort, selection_sort, quick_sort]:

    ttk.Label(root, text=func.__name__).pack()

    text.append(tk.Text(root, width=50, height=4, padx=10, wrap='char'))
    text[-1].pack()
    text[-1]['state'] = 'disabled'

    call(text[-1], func)


root.mainloop()
