import tkinter as tk
from tkinter import messagebox


def read_input_file():
    try:
        with open(input_file.get(), 'r') as f:
            data = f.read().split()
            if len(data) < 2:
                messagebox.showerror("Error", "Input file must contain at least two numbers")
                return
            num1.set(data[0])
            num2.set(data[1])
    except FileNotFoundError:
        messagebox.showerror("Error", "Input file not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def calculate():
    try:
        n1 = float(num1.get())
        n2 = float(num2.get())
        operation = var.get()

        if operation == "+":
            result = n1 + n2
        elif operation == "-":
            result = n1 - n2
        elif operation == "*":
            result = n1 * n2
        elif operation == "/":
            if n2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            else:
                result = n1 / n2

        label_result.config(text=str(result))
        with open(output_file.get(), 'w') as f:
            f.write(f"{n1} {operation} {n2} Result = {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Calculator")

label_input_file = tk.Label(root, text="Input file:")
label_input_file.grid(row=0, column=0)

input_file = tk.Entry(root)
input_file.grid(row=0, column=1)

button_read_file = tk.Button(root, text="Read file", command=read_input_file)
button_read_file.grid(row=0, column=2)

label_num1 = tk.Label(root, text="Number 1:")
label_num1.grid(row=1, column=0)

num1 = tk.StringVar()
entry_num1 = tk.Entry(root, textvariable=num1)
entry_num1.grid(row=1, column=1)

label_num2 = tk.Label(root, text="Number 2:")
label_num2.grid(row=2, column=0)

num2 = tk.StringVar()
entry_num2 = tk.Entry(root, textvariable=num2)
entry_num2.grid(row=2, column=1)

var = tk.StringVar(value="+")
radio_add = tk.Radiobutton(root, text="+", variable=var, value="+")
radio_add.grid(row=3, column=0)
radio_subtract = tk.Radiobutton(root, text="-", variable=var, value="-")
radio_subtract.grid(row=4, column=0)
radio_multiply = tk.Radiobutton(root, text="*", variable=var, value="*")
radio_multiply.grid(row=5, column=0)
radio_divide = tk.Radiobutton(root, text="/", variable=var, value="/")
radio_divide.grid(row=6, column=0)

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=7, column=0)

label_result_text = tk.Label(root, text="Result:")
label_result_text.grid(row=8, column=0)

label_result = tk.Label(root, text="")
label_result.grid(row=8, column=1)

label_output_file = tk.Label(root, text="Output file:")
label_output_file.grid(row=9, column=0)

output_file = tk.Entry(root)
output_file.insert(0, "output.txt")
output_file.grid(row=9, column=1)

root.mainloop()
