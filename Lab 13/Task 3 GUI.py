from enum import Enum
import tkinter as tk
from tkinter import ttk


class Cities(Enum):
    Київ = 1
    Львів = 2
    Одеса = 3
    Харків = 4
    Дніпро = 5
    Запоріжжя = 6
    Чернігів = 7
    Івано_Франківськ = 8
    Тернопіль = 9
    Черкаси = 10


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Enum GUI")
        self.geometry("300x400")

        self.label = tk.Label(self, text="Виберіть номер enum:")
        self.label.pack()

        self.enum_choice = tk.IntVar()
        combobox = ttk.Combobox(self, textvariable=self.enum_choice)
        combobox['values'] = [city.value for city in list(Cities)]
        combobox.pack()


        # for i, city in enumerate(Cities, 1):
        #     tk.Radiobutton(self, text=f"{i}: {city.name}", variable=self.enum_choice, value=i).pack()

        self.show_button = tk.Button(self, text="Повністю", command=self.show_full)
        self.show_button.pack()

        self.name_button = tk.Button(self, text="Ім'я", command=self.show_name)
        self.name_button.pack()

        self.value_button = tk.Button(self, text="Значення", command=self.show_value)
        self.value_button.pack()

        self.result = tk.StringVar()
        self.result.set("Результат відображатиметься тут")
        self.result_label = tk.Label(self, textvariable=self.result)
        self.result_label.pack()

    def show_full(self):
        pass
        index = self.enum_choice.get() - 1
        if 0 <= index < len(Cities):
            city = list(Cities)[index]
            self.result.set(city)

    def show_name(self):
        pass
        index = self.enum_choice.get() - 1
        if 0 <= index < len(Cities):
            city = list(Cities)[index]
            self.result.set(city.data)

    def show_value(self):
        pass
        index = self.enum_choice.get() - 1
        if 0 <= index < len(Cities):
            city = list(Cities)[index]
            self.result.set(city.value)


if __name__ == "__main__":
    app = GUI()
    app.mainloop()
