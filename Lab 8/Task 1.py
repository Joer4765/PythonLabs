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

output_text = tk.Text(root, width=20, height=3, padx=10)
output_text.pack()
output_text.focus()
output_text['state'] = 'disabled'


def func(input_array) -> list:
    for i in range(len(input_array)):
        for j in range(len(input_array[i])):
            if input_array[i][j].isdigit():
                input_array[i][j] = '!'
    return input_array


def call():
    output(output_text, matrix2text(func(text2matrix(get_input(input_text)))))


func_button = ttk.Button(root, text='DigsTo!', command=call)
func_button.pack()

root.mainloop()
