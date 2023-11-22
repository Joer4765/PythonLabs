import tkinter as tk
from random import randint


class Student:
    def __init__(self, age, course, name):
        self.age = age
        self.course = course
        self.name = name

    def __str__(self):
        return f"Ім'я: {self.name}, Вік: {self.age}, Курс: {self.course}"


# Функція для зміни властивостей об'єкта за вказаним номером
def modify_property(obj_num, obj_field, new_value):
    match obj_field:
        case 'вік':
            students[obj_num - 1].age = new_value
        case 'курс':
            students[obj_num - 1].course = new_value
        case "ім'я":
            students[obj_num - 1].name = new_value
    update_display()


# Функція для оновлення виведення в графічному інтерфейсі
def update_display():
    text.delete("1.0", tk.END)
    for i, student in enumerate(students, start=1):
        text.insert(tk.END, f"Об'єкт {i}: {str(student)}\n\n")


# Функція для обробки подій кнопок
def button_click():
    obj_num = int(entry_obj.get())
    obj_field = entry_property.get()
    new_value = entry_value.get()
    modify_property(obj_num, obj_field, new_value)


# Створення випадкового списку студентів
students = [Student(randint(18, 25), randint(1, 5), f"Student{i}") for i in range(5)]

# Створення графічного інтерфейсу
root = tk.Tk()
root.title("Зміна властивостей студента")

# Введення номеру об'єкта
label_obj = tk.Label(root, text="Введіть номер об'єкта:")
label_obj.pack()

entry_obj = tk.Entry(root)
entry_obj.pack()

# Введення номеру властивості
label_property = tk.Label(root, text="Введіть назву властивості (вік, курс чи ім'я):")
label_property.pack()

entry_property = tk.Entry(root)
entry_property.pack()

# Введення нового значення
label_value = tk.Label(root, text="Введіть нове значення:")
label_value.pack()

entry_value = tk.Entry(root)
entry_value.pack()

# Кнопка для виконання змін
button = tk.Button(root, text="Виконати зміни", command=button_click)
button.pack()

# Виведення результатів в графічному інтерфейсі
text = tk.Text(root)
text.pack()

update_display()

# Запуск головного циклу Tkinter
root.mainloop()
