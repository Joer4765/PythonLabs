import tkinter as tk
import re

def open_file():
    filepath = 'TF_3.txt'
    with open(filepath, 'r') as file:
        text = file.read()
    longest_words = find_longest_words(text)
    if longest_words:
        updated_text = replace_chars(text, longest_words)
        save_file(updated_text)
        display_message(f'The longest words in the file are "{", ".join(longest_words)}"')
    else:
        display_message('There are no words in the file')


def find_longest_words(text):
    words = re.findall(r'\b\w+\b', text)
    longest_words = []
    max_length = 0
    for word in words:
        length = len(word)
        if length > max_length:
            longest_words = [word]
            max_length = length
        elif length == max_length:
            longest_words.append(word)
    return longest_words


def replace_chars(text, words):
    for word in words:
        text = text.replace(word, '#' * len(word))
    return text


def save_file(text):
    filepath = 'TF_4.txt'
    with open(filepath, 'w') as file:
        file.write(text)


def display_message(message):
    message_label.config(text=message)


# Create GUI window
window = tk.Tk()
window.title('Longest Word Replacer')

# Add widgets to the window
open_button = tk.Button(window, text='Open File', command=open_file)
open_button.pack(padx=10, pady=10)

message_label = tk.Label(window, text='')
message_label.pack(padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
