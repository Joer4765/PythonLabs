import tkinter as tk
from tkinter import messagebox
import datetime


class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def __del__(self):
        messagebox.showinfo('Cleaning', f"Object with date {self.day}/{self.month}/{self.year} is being destroyed")

    def increase_year(self):
        self.year += 1

    def decrease_date(self):
        self.day -= 2
        if self.day < 1:
            self.month -= 1
            if self.month < 1:
                self.year -= 1
                self.month = 12
            if self.month in [1, 3, 5, 7, 8, 10, 12]:
                self.day = 31 + self.day
            elif self.month == 2:
                if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
                    self.day = 29 + self.day
                else:
                    self.day = 28 + self.day
            else:
                self.day = 30 + self.day

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"


class DateApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.date = None

        day_label = tk.Label(self, text="Day:")
        day_label.grid(row=0, column=0)
        self.day_entry = tk.Entry(self)
        self.day_entry.grid(row=0, column=1)

        month_label = tk.Label(self, text="Month:")
        month_label.grid(row=1, column=0)
        self.month_entry = tk.Entry(self)
        self.month_entry.grid(row=1, column=1)

        year_label = tk.Label(self, text="Year:")
        year_label.grid(row=2, column=0)
        self.year_entry = tk.Entry(self)
        self.year_entry.grid(row=2, column=1)

        create_button = tk.Button(self, text="Create Date", command=self.create_date)
        create_button.grid(row=3, column=0)

        delete_button = tk.Button(self, text="Delete Date", command=self.delete_date)
        delete_button.grid(row=3, column=1)

        increase_button = tk.Button(self, text="Increase Year", command=self.increase_year)
        increase_button.grid(row=4, column=0)

        decrease_button = tk.Button(self, text="Decrease Date", command=self.decrease_date)
        decrease_button.grid(row=4, column=1)

        self.label = tk.Label(self, text="")
        self.label.grid(row=6, column=0, columnspan=2)

    def create_date(self):
        try:
            day = int(self.day_entry.get())
            month = int(self.month_entry.get())
            year = int(self.year_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integer values for day, month and year.")
            return

        date = Date(day, month, year)

        self.date = date
        self.label.config(text=str(date))

    def delete_date(self):
        self.date = None
        self.label.config(text="")

    def increase_year(self):
        if self.date is not None:
            self.date.increase_year()
            self.label.config(text=str(self.date))

    def decrease_date(self):
        if self.date is not None:
            self.date.decrease_date()
            self.label.config(text=str(self.date))


class Employee(Date):
    def __init__(self, name, year, month, day):
        super().__init__(year, month, day)
        self.name = name

    def years_of_employment(self):
        current_year = int(datetime.date.today().year)

        delta = current_year - self.year
        return delta

    def __str__(self):
        return f"Name: {self.name}, Employment Date: {self.year}/{self.month}/{self.day}"


class EmployeeApp(DateApp):
    def __init__(self):
        super().__init__()
        self.employee = None

        name_label = tk.Label(self, text="Name:")
        name_label.grid(row=5, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=5, column=1)

        create_button = tk.Button(self, text="Create Employee", command=self.create_employee)
        create_button.grid(row=6, column=0)

        years_button = tk.Button(self, text="Years of Employment", command=self.years_of_employment)
        years_button.grid(row=6, column=1)

        self.label = tk.Label(self, text="")
        self.label.grid(row=7, column=0, columnspan=2)

    def create_employee(self):
        name = self.name_entry.get()
        year = int(self.year_entry.get())
        month = int(self.month_entry.get())
        day = int(self.day_entry.get())
        self.employee = Employee(name, year, month, day)
        self.label.config(text=str(self.employee))

    def years_of_employment(self):
        if self.employee is not None:
            years = self.employee.years_of_employment()
            self.label.config(text=f"Years of Employment: {years}")


if __name__ == "__main__":
    app = EmployeeApp()
    app.mainloop()

