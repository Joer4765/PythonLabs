import tkinter as tk
from tkinter import ttk
from help_funcs import *
import re

root = tk.Tk()
root.geometry('400x350')

input_label = ttk.Label(root, text='Input: ')
input_label.pack()

input_text = tk.Text(root, width=30, height=3, padx=10)
input_text.pack()
input_text.focus()


def replace_i(pattern: str, repl: str, i: int, s: str) -> str:
    count = 0
    result = ""
    for match in re.finditer(pattern, s):
        result += s[:re.search(pattern, s).start()]
        count += 1
        if count == i:
            result += repl
        else:
            result += match.group()
        s = s[match.end():]
    return result + s


def count_match(pattern: str, s: str):
    return len(re.findall(r'(?:[\dA-F]{2}\.){3}[\dA-F]{2}', s))


input_label = ttk.Label(root, text='Enter subtext i: ')
input_label.pack()

i = tk.Text(root, width=30, height=1, padx=10)
i.pack()

input_label = ttk.Label(root, text='Enter replacement: ')
input_label.pack()

repl = tk.Text(root, width=30, height=1, padx=10)
repl.pack()

count_label = ttk.Label(root, text='Count of matches: ')
count_label.pack()

count_text = tk.Text(root, width=30, height=1, padx=10)
count_text.pack()
count_text['state'] = 'disabled'

output_label = ttk.Label(root, text='Output: ')
output_label.pack()

output_text = tk.Text(root, width=30, height=3, padx=10)
output_text.pack()
output_text['state'] = 'disabled'

pattern = r'(?:[\dA-F]{2}\.){3}[\dA-F]{2}'

button = ttk.Button(root, text='count_match',
                    command=lambda: output(count_text,
                                           count_match(pattern, get_input(input_text))))
button.pack()

button = ttk.Button(root, text='replace_i',
                    command=lambda: output(output_text,
                                           replace_i(pattern,
                                                     repl=get_input(repl),
                                                     i=int(get_input(i)),
                                                     s=get_input(input_text))))
button.pack()

root.mainloop()
