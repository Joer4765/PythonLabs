import tkinter as tk
from tkinter import ttk
import csv


def get_input(text) -> str:
    return text.get('1.0', 'end-1c')


def output(text_obj, text):
    text_obj['state'] = 'normal'
    text_obj.replace('1.0', 'end', text)
    text_obj['state'] = 'disabled'


def matrix2text(matrix: list) -> str:
    return '\n'.join(map(str, (' '.join(x) for x in matrix)))


def arr2text(arr: list) -> str:
    formatted_data = []
    labels = [
        "Прізвище", "Ім’я", "По-батькові", "Поштовий індекс", "Країна",
        "Область", "Місто", "Вулиця", "Будинок", "Квартира",
        "Рік народження", "Рік працевлаштування"
    ]

    for entry in arr:
        formatted_entry = [f"{label}: {value}" for label, value in zip(labels, entry)]
        formatted_data.append("\n".join(formatted_entry))

    return '\n\n'.join(formatted_data)
    # return '\n'.join(map(str, arr))


def text2matrix(text: str) -> list:
    return [row.split() for row in text.split('\n')]


def func(filename) -> list:
    # define number of parameters
    num_params = 12

    # read data from CSV file into array
    data = []
    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == num_params:
                data.append(row)

    # process data
    result = []
    for security in data:
        if int(2023 - int(security[-1])) > 10:
            result.append(security)

    return result


def write_to_csv(data, output_filename):
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


root = tk.Tk()

input_label = ttk.Label(root, text='Filename: ')
input_label.pack()

input_text = tk.Text(root, width=30, height=1, padx=10)
input_text.pack()
input_text.focus()

output_label = ttk.Label(root, text='Output: ')
output_label.pack()

output_text = tk.Text(root, width=50, height=30, padx=10, wrap='none')
xs = ttk.Scrollbar(root, orient='horizontal', command=output_text.xview)
output_text['xscrollcommand'] = xs.set
output_text.pack()
xs.pack()
output_text['state'] = 'disabled'


def func_button_click():
    input_filename = get_input(input_text)
    result = func(input_filename)
    output(output_text, arr2text(result))
    output_filename = "output.csv"
    write_to_csv(result, output_filename)
    output_text.insert(tk.END, f"\n\nResult written to {output_filename}")


func_button = ttk.Button(root, text='Func', command=func_button_click)
func_button.pack()

root.mainloop()

#
# import tkinter as tk
# from tkinter import ttk
# import csv
#
# def get_input(text) -> str:
#     return text.get('1.0', 'end-1c')
#
# def output(text_obj, text):
#     text_obj['state'] = 'normal'
#     text_obj.replace('1.0', 'end', text)
#     text_obj['state'] = 'disabled'
#
# def arr2text(arr: list) -> str:
#     formatted_data = []
#     labels = [
#         "Прізвище", "Ім’я", "По-батькові", "Поштовий індекс", "Країна",
#         "Область", "Район", "Місто", "Вулиця", "Будинок", "Квартира",
#         "Рік народження", "Рік працевлаштування"
#     ]
#
#     for entry in arr:
#         formatted_entry = [f"{label}: {value}" for label, value in zip(labels, entry)]
#         formatted_data.append("\n".join(formatted_entry))
#
#     return '\n\n'.join(formatted_data)
#
# def func(filename) -> list:
#     # define number of parameters
#     num_params = 10
#
#     # read data from CSV file into array
#     data = []
#     with open(filename, 'r', newline='') as f:
#         reader = csv.reader(f, delimiter=';')
#         for row in reader:
#             if len(row) == num_params:
#                 data.append(row)
#
#     return data
#
# root = tk.Tk()
#
# input_label = ttk.Label(root, text='Filename: ')
# input_label.pack()
#
# input_text = tk.Text(root, width=30, height=1, padx=10)
# input_text.pack()
# input_text.focus()
#
# output_label = ttk.Label(root, text='Output: ')
# output_label.pack()
#
# output_text = tk.Text(root, width=80, height=15, padx=10, wrap='none')
# ys = ttk.Scrollbar(root, orient='vertical', command=output_text.yview)
# output_text['yscrollcommand'] = ys.set
# output_text.pack()
# ys.pack()
# output_text['state'] = 'disabled'
#
# def func_button_click():
#     input_filename = get_input(input_text)
#     result = func(input_filename)
#     output(output_text, arr2text(result))
#
# func_button = ttk.Button(root, text='Func', command=func_button_click)
# func_button.pack()
#
# root.mainloop()
