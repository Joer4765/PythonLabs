import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task 4 GUI")
        self.geometry("825x550")

        self.product_data = []

        self.product_list = ttk.Treeview(self, columns=("Name", "Price", "Category", "Demand"), show="headings")
        self.product_list.heading("Name", text="Назва продукту")
        self.product_list.heading("Price", text="Ціна")
        self.product_list.heading("Category", text="Категорія")
        self.product_list.heading("Demand", text="Попит")

        self.name_entry = tk.Entry(self, width=20)
        self.price_entry = tk.Entry(self, width=10)
        self.category_entry = tk.Entry(self, width=20)
        self.demand_entry = tk.Entry(self, width=10)

        self.add_button = tk.Button(self, text="Додати", command=self.add_product)

        self.analyze_button = tk.Button(self, text="Аналізувати", command=self.analyze)
        self.result_text = tk.Label(self, text="", padx=10, pady=10)

        self.product_list.pack(pady=10)

        tk.Label(self, text="Назва продукту").pack()
        self.name_entry.pack()
        tk.Label(self, text="Ціна").pack()
        self.price_entry.pack()
        tk.Label(self, text="Категорія").pack()
        self.category_entry.pack()
        tk.Label(self, text="Попит").pack()
        self.demand_entry.pack()

        self.add_button.pack()
        self.analyze_button.pack()
        self.result_text.pack()

    def add_product(self):
        name = self.name_entry.get()
        price = float(self.price_entry.get())
        category = self.category_entry.get()
        demand = float(self.demand_entry.get())

        new_product = (name, price, category, demand)
        self.product_data.append(new_product)

        self.product_list.insert("", "end", values=new_product)

        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.demand_entry.delete(0, tk.END)

    def analyze(self):
        average_price = sum([product[1] for product in self.product_data]) / len(self.product_data)
        social_products = [product for product in self.product_data if product[1] < average_price]
        result_text = f"Кількість продуктів у соціальній категорії: {len(social_products)}"
        self.result_text.config(text=result_text)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
