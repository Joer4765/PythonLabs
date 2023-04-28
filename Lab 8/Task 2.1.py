import tkinter as tk
from tkinter import ttk
from help_funcs import *

root = tk.Tk()

input_label = ttk.Label(root, text='Enter name 1: ')
input_label.pack()

input_text1 = tk.Text(root, width=30, height=3, padx=10)
input_text1.pack()
input_text1.focus()

input_label = ttk.Label(root, text='Enter name 2: ')
input_label.pack()

input_text2 = tk.Text(root, width=30, height=3, padx=10)
input_text2.pack()

output_label = ttk.Label(root, text='Output: ')
output_label.pack()

output_text = tk.Text(root, width=30, height=3, padx=10)
output_text.pack()
output_text['state'] = 'disabled'


def func(s1, s2) -> str:
    return f'{s1} + {s2} = Кохання'


def call():
    output(output_text, func(get_input(input_text1), get_input(input_text2)))


func_button = ttk.Button(root, text='Ship', command=call)
func_button.pack()

root.mainloop()
