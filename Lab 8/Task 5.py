import tkinter as tk
from tkinter import ttk
from help_funcs import *
import re

root = tk.Tk()

input_label = ttk.Label(root, text='Enter str: ')
input_label.pack()

input_text = tk.Text(root, width=50, height=20, padx=10, wrap='word')
input_text.pack()
input_text.focus()

output_label = ttk.Label(root, text='Output: ')
output_label.pack()

output_text = tk.Text(root, width=50, height=5, padx=10, wrap='word')
output_text.pack()
output_text['state'] = 'disabled'


def func(s) -> str:

    # Split the text into words
    words = re.findall(r'\b\w+\b', s)

    # Create a dictionary to store words by length
    word_dict = {}
    for word in words:
        if len(word) not in word_dict:
            word_dict[len(word)] = []
        word_dict[len(word)].append(word)

    # Find the longest chain of words with the same length
    longest_chain = ""
    for word_length in word_dict:
        chain = " ".join(word_dict[word_length])
        if len(chain) > len(longest_chain):
            longest_chain = chain

    return longest_chain


func_button = ttk.Button(root, text='Func', command=lambda: output(output_text, func(get_input(input_text))))
func_button.pack()

root.mainloop()
