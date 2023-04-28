import tkinter as tk


class DistanceCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Distance Calculator")

        self.speed_label = tk.Label(master, text="Speed (m/s):")
        self.speed_entry = tk.Entry(master)

        self.time_label = tk.Label(master, text="Time (minutes):")
        self.time_entry = tk.Entry(master)

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.result_label = tk.Label(master, text="Distance (m):")
        self.result_text = tk.Label(master)

        self.speed_label.grid(row=0, column=0)
        self.speed_entry.grid(row=0, column=1)
        self.time_label.grid(row=1, column=0)
        self.time_entry.grid(row=1, column=1)
        self.calculate_button.grid(row=2, columnspan=2)
        self.result_label.grid(row=3, column=0)
        self.result_text.grid(row=3, column=1)

    def calculate(self):
        speed = float(self.speed_entry.get())
        time = float(self.time_entry.get()) * 60
        distance = speed * time
        self.result_text.config(text=str(distance))


root = tk.Tk()
my_calculator = DistanceCalculator(root)
root.mainloop()
