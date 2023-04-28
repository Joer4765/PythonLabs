import tkinter as tk
from tkinter import ttk
from function import *
from help_funcs import *

root = tk.Tk()

input_label = ttk.Label(root, text='Input: ')
input_label.pack()

input_text = tk.Text(root, width=20, height=3, padx=10)
input_text.pack()
input_text.focus()

output_label = ttk.Label(root, text='Output: ')
output_label.pack()

output_text = tk.Text(root, width=20, height=1, padx=10)
output_text.pack()
output_text.focus()
output_text['state'] = 'disabled'


def call():
    output(output_text, arr2text(func(text2matrix(get_input(input_text)))))


func_button = ttk.Button(root, text='Function', command=call)
func_button.pack()

root.mainloop()
