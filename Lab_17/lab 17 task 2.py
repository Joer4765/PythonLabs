import tkinter as tk
from random import Random
from functools import reduce
from numpy import take


def generate_random_array():
    n = int(entry.get())
    array = [0] * n
    rand = Random()
    total = 0
    a = int(a_entry.get())
    b = int(b_entry.get())

    result_text.config(state="normal")
    result_text.delete(1.0, tk.END)

    result_text.insert(tk.END, "Input massive:\n")
    for i in range(n):
        array[i] = rand.randint(-9, 10)
        result_text.insert(tk.END, f"{array[i]} ")
        total += array[i]
    result_text.insert(tk.END, "\n")

    avg = total / n
    result_text.insert(tk.END, f"Average = {avg}\n")

    # minus avg
    result_text.insert(tk.END, "El - avg:\n")
    res = map(lambda x: x - avg, array)
    result_text.insert(tk.END, ' '.join(map(str, res)) + '\n\n')

    # count of greater then avg
    result_text.insert(tk.END, "Count of greater then avg:\n")
    res = len(list(filter(lambda x: x > avg, array)))
    result_text.insert(tk.END, str(res) + '\n\n')
    print()

    # arr sum is double digit
    result_text.insert(tk.END, "Is arr sum double digit:\n")
    res = 10 <= reduce(lambda a, b: a + b, array) <= 100
    result_text.insert(tk.END, ('Arr sum is double digit' if res else 'Arr sum is not double digit') + '\n\n')

    # count not in interval
    result_text.insert(tk.END, "Count not in interval:\n")
    res = len(take(array, range(len(array) - (b - a))))
    result_text.insert(tk.END, str(res) + '\n\n')
    result_text.config(state="disabled")


def minus_avg(arr, avg):
    result = []
    for i in range(len(arr)):
        result[i] = round(arr[i] - avg, 2)
    return result


root = tk.Tk()
root.title("Random Array Generator")

label = tk.Label(root, text="Enter n:")
label.pack()

entry = tk.Entry(root)
entry.pack()

label = tk.Label(root, text="Enter a:")
label.pack()

a_entry = tk.Entry(root)
a_entry.pack()

label = tk.Label(root, text="Enter b:")
label.pack()

b_entry = tk.Entry(root)
b_entry.pack()

generate_button = tk.Button(root, text="Generate Random Array", command=generate_random_array)
generate_button.pack()

result_text = tk.Text(root, height=10, width=40, state="disabled")
result_text.pack()

root.mainloop()
