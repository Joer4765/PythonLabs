import tkinter as tk
from tkinter import ttk
from help_funcs import *

root = tk.Tk()

input_label = ttk.Label(root, text='Filename: ')
input_label.pack()

input_text = tk.Text(root, width=30, height=1, padx=10)
input_text.pack()
input_text.focus()

output_label = ttk.Label(root, text='Output: ')
output_label.pack()

output_text = tk.Text(root, width=50, height=10, padx=10, wrap='none')
xs = ttk.Scrollbar(root, orient='horizontal', command=output_text.xview)
output_text['xscrollcommand'] = xs.set
output_text.pack()
xs.pack()
output_text['state'] = 'disabled'


def func(filename) -> str:
    # define number of parameters
    num_params = 10

    # read data from file into array
    data = []
    with open(filename, 'r') as f:
        for line in f:
            params = line.strip().split(';')
            if len(params) == num_params:
                data.append(params)

    # process data
    result = []
    for security in data:
        if int(2023 - int(security[-1])) > 10:
            result.append(security)

    return result


func_button = ttk.Button(root, text='Func', command=lambda: output(output_text, arr2text(func(get_input(input_text)))))
func_button.pack()

root.mainloop()
