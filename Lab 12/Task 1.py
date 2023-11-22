import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from abc import ABC, abstractmethod


class Plant(ABC):
    def __init__(self, name, red_book):
        self.name = name
        self.red_book = red_book

    @abstractmethod
    def display_information(self):
        pass

    @abstractmethod
    def bloom(self):
        pass

    def grow(self):
        print(f"{self.name} is growing.")


class Tree(Plant):
    def __init__(self, name, red_book, height):
        super().__init__(name, red_book)
        self.height = height

    def display_information(self):
        messagebox.showinfo('', f"{self.name} is a tree that can grow up to {self.height} meters tall.")

    def bloom(self):
        messagebox.showinfo('', f"{self.name} is not blooming.")

    def shed_leaves(self):
        messagebox.showinfo('', f"{self.name} is shedding its leaves.")


class Flower(Plant):
    def __init__(self, name, red_book, color):
        super().__init__(name, red_book)
        self.color = color

    def display_information(self):
        messagebox.showinfo('', f"{self.name} is a {self.color} flower.")

    def bloom(self):
        messagebox.showinfo('', f"{self.name} is blooming.")


class PlantGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Plant Database")

        self.plants = []

        self.name_label = ttk.Label(self.window, text="Name:")
        self.name_label.grid(column=0, row=0)
        self.name_entry = ttk.Entry(self.window)
        self.name_entry.grid(column=1, row=0)

        self.type_label = ttk.Label(self.window, text="Type:")
        self.type_label.grid(column=0, row=1)
        self.type_combobox = ttk.Combobox(self.window, values=["Tree", "Flower"])
        self.type_combobox.grid(column=1, row=1)

        self.attribute_label = ttk.Label(self.window, text="Height/Color:")
        self.attribute_label.grid(column=0, row=2)
        self.attribute_entry = ttk.Entry(self.window)
        self.attribute_entry.grid(column=1, row=2)

        self.is_in_red_book = tk.BooleanVar()
        self.c1 = tk.Checkbutton(self.window, text='Is in Red Book?',
                                 variable=self.is_in_red_book, onvalue=True, offvalue=False)
        self.c1.grid(column=0, row=3)

        self.add_button = ttk.Button(self.window, text="Add Plant", command=self.add_plant)
        self.add_button.grid(column=0, row=4)

        self.display_button = ttk.Button(self.window, text="Display Plants", command=self.display_plants)
        self.display_button.grid(column=1, row=4)

        self.read_book_button = ttk.Button(self.window, text="Search Red Book", command=self.search_red_book)
        self.read_book_button.grid(column=0, row=5, columnspan=2)

    def search_red_book(self):
        s = 'Plants in Red Book: '
        for p in self.plants:
            if p.red_book:
                s += p.data + ' '
        messagebox.showinfo('', s)

    def add_plant(self):
        name = self.name_entry.get()
        plant_type = self.type_combobox.get()
        attribute = self.attribute_entry.get()

        if plant_type == "Tree":
            height = int(attribute)
            tree = Tree(name, height=height, red_book=self.is_in_red_book)
            self.plants.append(tree)
        elif plant_type == "Flower":
            color = attribute
            flower = Flower(name, color=color, red_book=self.is_in_red_book)
            self.plants.append(flower)

    def display_plants(self):
        for plant in self.plants:
            plant.display_information()

    def run(self):
        self.window.mainloop()


gui = PlantGUI()
gui.run()
