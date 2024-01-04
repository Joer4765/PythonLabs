import tkinter as tk
import re


def create_file(input_file):
    with open(input_file, 'w') as tf_1:
        print(
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce malesuada auctor ipsum, vel accumsan odio tincidunt a. Sed semper nisl eget nisi commodo, a consectetur dolor hendrerit. Nunc eu sapien euismod, imperdiet quam ac, fringilla turpis. Duis non diam non nisl pellentesque convallis. Sed semper turpis vel velit elementum malesuada. Sed vulputate auctor nisi, sed posuere lorem tincidunt vel. Suspendisse semper ultrices dolor, vel elementum eros lacinia eu. Ut rutrum massa vel risus vestibulum, ac tincidunt quam vehicula. Sed mollis aliquet erat ut commodo. Mauris ornare eget enim id faucibus. Vivamus interdum risus sed felis accumsan, ac suscipit elit dictum.',
            file=tf_1)
    process_file_button.configure(state=tk.NORMAL)


def process_file(input_file):
    with open(input_file, 'r') as tf_1, open('TF_2.txt', 'w') as tf_2:
        words_with_a = []
        tf_1 = tf_1.read()
        words = re.findall(r'\b\w+\b', tf_1)
        for word in words:
            if 'a' in word:
                words_with_a.append(word)
        if words_with_a:
            tf_2.write('\n'.join(words_with_a))
        else:
            tf_2.write('No words with "a" found in the file.')

    with open('TF_2.txt', 'r') as tf_2:
        output = tf_2.read()
        output_label.configure(text=output)


root = tk.Tk()
root.title('File Processing App')

input_file = 'TF_1.txt'

create_file_button = tk.Button(root, text='Create file', command=lambda: create_file(input_file))
create_file_button.pack()

process_file_button = tk.Button(root, text='Process file', command=lambda: process_file(input_file), state=tk.DISABLED)
process_file_button.pack()

quit_button = tk.Button(root, text='Quit', command=root.destroy)
quit_button.pack()

output_label = tk.Label(root)
output_label.pack()

root.mainloop()
