import tkinter as tk
from tkinter import ttk


class SatelliteDish:
    def __init__(self, diameter, material, price):
        self.diameter = diameter
        self.material = material
        self.price = price

    def quality(self):
        return self.diameter / self.price

    def __str__(self):
        return f'Diameter: {self.diameter}, Material: {self.material}, Price: {self.price}'


class SatelliteDish2(SatelliteDish):
    def __init__(self, diameter, material, price, mount_type):
        super().__init__(diameter, material, price)
        self.mount_type = mount_type

    def quality(self):
        q = super().quality()
        if self.mount_type == 'azimuthal':
            return q
        elif self.mount_type == 'polar':
            return 2 * q
        elif self.mount_type == 'toroidal':
            return 2.5 * q

    def __str__(self):
        return super().__str__() + f', Mount Type: {self.mount_type}'


class App:
    def __init__(self, master):
        self.master = master
        master.title('Satellite Dish')

        self.diameter_label = ttk.Label(master, text='Diameter:')
        self.diameter_label.grid(row=0, column=0)
        self.diameter_entry = ttk.Entry(master)
        self.diameter_entry.grid(row=0, column=1)

        self.material_label = ttk.Label(master, text='Material:')
        self.material_label.grid(row=1, column=0)
        self.material_entry = ttk.Entry(master)
        self.material_entry.grid(row=1, column=1)

        self.price_label = ttk.Label(master, text='Price:')
        self.price_label.grid(row=2, column=0)
        self.price_entry = ttk.Entry(master)
        self.price_entry.grid(row=2, column=1)

        self.mount_type_label = ttk.Label(master, text='Mount Type:')
        self.mount_type_label.grid(row=3, column=0)

        self.mount_type = tk.StringVar(self.master)
        self.mount_type_menu = tk.OptionMenu(self.master, self.mount_type, "", "azimuthal", "polar", "toroidal")
        self.mount_type_menu.grid(row=3, column=1)

        self.create_button = ttk.Button(master, text='Create', command=self.create_dish)
        self.create_button.grid(row=4, column=0)

        self.output_label = ttk.Label(master, text='')
        self.output_label.grid(row=5, column=0, columnspan=2)

    def create_dish(self):
        diameter = int(self.diameter_entry.get())
        material = self.material_entry.get()
        price = int(self.price_entry.get())
        mount_type = self.mount_type.get()
        if mount_type:
            dish = SatelliteDish2(diameter, material, price, mount_type)
        else:
            dish = SatelliteDish(diameter, material, price)
        self.output_label['text'] = f'{dish}\nQuality: {dish.quality()}'


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()

