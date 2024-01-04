import tkinter as tk


# Функція вищого порядку
def calculate(operation, x, y):
    return operation(x, y)


def calculate_curry(operation):
    def curried(x):
        def inner(y):
            return calculate(operation, x, y)

        return inner

    return curried


def get_operation():
    return {'Додавання': lambda x, y: x + y, 'Множення': lambda x, y: x * y, 'Віднімання': lambda x, y: x - y,
            'Ділення': lambda x, y: x / y if y else None}[operation_var.get()]


# Створення GUI з допомогою tkinter
def on_calculate():
    operation = get_operation()
    x = int(x_entry.get())
    y = int(y_entry.get())
    result = calculate(operation, x, y)
    result_label.config(text=f"Результат: {result}")


def on_calculate_curry():
    operation = get_operation()
    x = int(x_entry.get())
    y = int(y_entry.get())
    result = calculate_curry(operation)(x)(y)
    result_label.config(text=f"Результат: {result}")


root = tk.Tk()
root.title("Калькулятор")

# Вибір операції
operation_var = tk.StringVar(root)
operation_var.set('Додавання')
operation_label = tk.Label(root, text="Виберіть операцію:")
operation_menu = tk.OptionMenu(root, operation_var, 'Додавання', 'Множення', 'Віднімання', 'Ділення')
operation_label.pack()
operation_menu.pack()

# Введення чисел
x_label = tk.Label(root, text="Введіть перше число:")
x_entry = tk.Entry(root)
y_label = tk.Label(root, text="Введіть друге число:")
y_entry = tk.Entry(root)
x_label.pack()
x_entry.pack()
y_label.pack()
y_entry.pack()

# Результат
result_label = tk.Label(root, text="")
result_label.pack()

# Кнопка обчислення
calculate_button = tk.Button(root, text="Обчислити", command=on_calculate)
calculate_button.pack()
calculate_button = tk.Button(root, text="Обчислити (curry)", command=on_calculate_curry)
calculate_button.pack()

# Запуск GUI
root.mainloop()
