import tkinter as tk
from tkinter import ttk
from help_funcs import *
import re

root = tk.Tk()

input_label = ttk.Label(root, text='Enter str: ')
input_label.pack()

input_text = tk.Text(root, width=30, height=3, padx=10)
input_text.pack()
input_text.focus()

output_label = ttk.Label(root, text='Output: ')
output_label.pack()

output_text = tk.Text(root, width=30, height=3, padx=10)
output_text.pack()
output_text['state'] = 'disabled'


def func(s) -> str:
    return re.sub(r'\b[A-Za-z]+\b', '...', s)


func_button = ttk.Button(root, text='Func', command=lambda: output(output_text, func(get_input(input_text))))
func_button.pack()

root.mainloop()
