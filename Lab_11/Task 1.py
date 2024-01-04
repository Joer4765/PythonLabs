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

    def calculate(self):
        speed = float(self.speed_entry.get())
        time = float(self.time_entry.get()) * 60
        distance = speed * time
        self.result_text.config(text=str(distance))


class WorkCalculator(DistanceCalculator):
    def __init__(self, master):
        super().__init__(master)

        self.speed_label = tk.Label(master, text="Speed:")
        self.speed_entry = tk.Entry(master)

        self.time_label = tk.Label(master, text="Time:")
        self.time_entry = tk.Entry(master)

        self.force_label = tk.Label(master, text="Force:")
        self.force_entry = tk.Entry(master)

        self.work_label = tk.Label(master, text="Work:")
        self.work_text = tk.Label(master)

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.result_label = tk.Label(master, text="Distance:")
        self.result_text = tk.Label(master)

        self.speed_label.grid(row=0, column=0)
        self.speed_entry.grid(row=0, column=1)
        self.time_label.grid(row=1, column=0)
        self.time_entry.grid(row=1, column=1)
        self.force_label.grid(row=2, column=0)
        self.force_entry.grid(row=2, column=1)
        self.calculate_button.grid(row=3, columnspan=2)
        self.result_label.grid(row=4, column=0)
        self.result_text.grid(row=4, column=1)
        self.work_label.grid(row=5, column=0)
        self.work_text.grid(row=5, column=1)

    def calculate(self):
        super().calculate()
        speed = float(self.speed_entry.get())
        time = float(self.time_entry.get()) * 60
        distance = speed * time
        work = distance * float(self.force_entry.get())
        self.work_text.config(text=str(work))


root = tk.Tk()
my_calculator = WorkCalculator(root)
root.mainloop()
