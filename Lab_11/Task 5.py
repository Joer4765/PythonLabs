import tkinter as tk


class Plane:
    def __init__(self, brand, model, max_speed, max_altitude):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed
        self.max_altitude = max_altitude

    def cost(self):
        return self.max_speed * 1000 + self.max_altitude * 100

    def info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Max Speed: {self.max_speed}, Cost: {self.cost()}"


class Bomber(Plane):
    def __init__(self, brand, model, max_speed, max_altitude, pilot_name):
        super().__init__(brand, model, max_speed, max_altitude)
        self.pilot_name = pilot_name

    def cost(self):
        return super().cost() * 2

    def info(self):
        return f'{super().info()} Pilot Name: {self.pilot_name}'


class Fighter(Plane):
    def __init__(self, brand, model, max_speed, max_altitude, assignment_group):
        super().__init__(brand, model, max_speed, max_altitude)
        self.assignment_group = assignment_group

    def cost(self):
        return super().cost() * 3

    def info(self):
        return f'{super().info()} Assignment Group: {self.assignment_group}'


class App:
    def __init__(self, master):
        self.master = master
        master.title("Plane Information")

        self.plane_list = []

        self.brand_label = tk.Label(master, text="Brand")
        self.brand_entry = tk.Entry(master)

        self.model_label = tk.Label(master, text="Model")
        self.model_entry = tk.Entry(master)

        self.max_speed_label = tk.Label(master, text="Max Speed")
        self.max_speed_entry = tk.Entry(master)

        self.max_altitude_label = tk.Label(master, text="Max Altitude")
        self.max_altitude_entry = tk.Entry(master)

        self.pilot_name_label = tk.Label(master, text="Pilot Name (Bomber only)")
        self.pilot_name_entry = tk.Entry(master)

        self.assignment_group_label = tk.Label(master, text="Assignment Group (Fighter only)")
        self.assignment_group_entry = tk.Entry(master)

        self.plane_type_label = tk.Label(master, text="Plane Type")
        self.plane_type_var = tk.StringVar()
        self.plane_type_var.set("Plane")
        self.plane_type_option_menu = tk.OptionMenu(
            master,
            self.plane_type_var,
            "Plane",
            "Bomber",
            "Fighter"
        )

        self.create_button = tk.Button(
            master,
            text="Create Plane",
            command=self.create_plane
        )

        self.info_label = tk.Label(
            master,
            text="Plane Information"
        )

        # Layout
        self.brand_label.grid(row=0, column=0)
        self.brand_entry.grid(row=0, column=1)

        self.model_label.grid(row=1, column=0)
        self.model_entry.grid(row=1, column=1)

        self.max_speed_label.grid(row=2, column=0)
        self.max_speed_entry.grid(row=2, column=1)

        self.max_altitude_label.grid(row=3, column=0)
        self.max_altitude_entry.grid(row=3, column=1)

        self.pilot_name_label.grid(row=4, column=0)
        self.pilot_name_entry.grid(row=4, column=1)

        self.assignment_group_label.grid(row=5, column=0)
        self.assignment_group_entry.grid(row=5, column=1)

        self.plane_type_label.grid(row=6, column=0)
        self.plane_type_option_menu.grid(row=6, column=1)

        self.create_button.grid(row=7, column=0, columnspan=2)

        self.info_label.grid(row=8, column=0, columnspan=2)

    def create_plane(self):
        global plane
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        max_speed = int(self.max_speed_entry.get())
        max_altitude = int(self.max_altitude_entry.get())
        pilot_name = self.pilot_name_entry.get()
        assignment_group = self.assignment_group_entry.get()
        plane_type = self.plane_type_var.get()

        if plane_type == "Plane":
            plane = Plane(brand, model, max_speed, max_altitude)
        elif plane_type == "Bomber":
            plane = Bomber(brand, model, max_speed, max_altitude, pilot_name)
        elif plane_type == "Fighter":
            plane = Fighter(brand, model, max_speed, max_altitude, assignment_group)

        self.plane_list.append(plane)

        info_text = "\n".join([plane.info() for plane in self.plane_list])
        self.info_label["text"] = info_text


root = tk.Tk()
app = App(root)
root.mainloop()
