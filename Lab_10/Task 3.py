import tkinter as tk


class Bicycle:
    def __init__(self):
        self._brand = ""
        self._model = ""
        self._wheel_size = 0
        self._frame_size = 0
        self._color = ""
        self._weight = 0
        self._price = 0

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def wheel_size(self):
        return self._wheel_size

    @wheel_size.setter
    def wheel_size(self, value):
        self._wheel_size = value

    @property
    def frame_size(self):
        return self._frame_size

    @frame_size.setter
    def frame_size(self, value):
        self._frame_size = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @staticmethod
    def ride():
        return "Riding the bicycle"

    @staticmethod
    def ring_bell():
        return "Ring ring!"

    @staticmethod
    def brake():
        return "Braking the bicycle"


def on_submit():
    bike = Bicycle()
    bike.brand = brand_entry.get()
    bike.model = model_entry.get()
    bike.wheel_size = int(wheel_size_entry.get())
    bike.frame_size = int(frame_size_entry.get())
    bike.color = color_entry.get()
    bike.weight = float(weight_entry.get())
    bike.price = float(price_entry.get())

    result_label["text"] = f"Brand: {bike.brand}\n" \
                           f"Model: {bike.model}\n" \
                           f"Wheel size: {bike.wheel_size}\n" \
                           f"Frame size: {bike.frame_size}\n" \
                           f"Color: {bike.color}\n" \
                           f"Weight: {bike.weight}\n" \
                           f"Price: {bike.price}\n" \
                           f"{bike.ride()}\n" \
                           f"{bike.ring_bell()}\n" \
                           f"{bike.brake()} "


root = tk.Tk()

brand_label = tk.Label(root, text="Brand:")
brand_label.pack()

brand_entry = tk.Entry(root)
brand_entry.pack()

model_label = tk.Label(root, text="Model:")
model_label.pack()

model_entry = tk.Entry(root)
model_entry.pack()

wheel_size_label = tk.Label(root, text="Wheel size:")
wheel_size_label.pack()

wheel_size_entry = tk.Entry(root)
wheel_size_entry.pack()

frame_size_label = tk.Label(root, text="Frame size:")
frame_size_label.pack()

frame_size_entry = tk.Entry(root)
frame_size_entry.pack()

color_label = tk.Label(root, text="Color:")
color_label.pack()

color_entry = tk.Entry(root)
color_entry.pack()

weight_label = tk.Label(root, text="Weight:")
weight_label.pack()

weight_entry = tk.Entry(root)
weight_entry.pack()

price_label = tk.Label(root, text="Price:")
price_label.pack()

price_entry = tk.Entry(root)
price_entry.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
