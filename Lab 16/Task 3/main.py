import tkinter as tk
from tkinter import messagebox
from binarytree import BinaryTree


class TreeGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x200')
        self.root.title("Binary Search Tree")
        self.tree = BinaryTree()

        self.label = tk.Label(root, text="Number:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.label = tk.Label(root, text="Title:")
        self.label.pack()

        self.title_entry = tk.Entry(root)
        self.title_entry.pack()

        self.insert_button = tk.Button(root, text="Insert", command=self.insert)
        self.insert_button.pack()

        self.delete_button = tk.Button(root, text="Delete", command=self.delete)
        self.delete_button.pack()

        self.search_button = tk.Button(root, text="Search", command=self.search)
        self.search_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.tree_display = tk.Label(root, text="")
        self.tree_display.pack()

    def insert(self):
        try:
            key = int(self.entry.get())
            string = self.title_entry.get()
            self.tree.insert(key, string)
            self.update_tree_display()
            self.update_result_label("Insertion successful.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")

    def delete(self):
        try:
            key = int(self.entry.get())
            self.tree.delete(key)
            self.entry.delete(0, tk.END)
            self.update_tree_display()
            self.update_result_label("Deletion successful.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")

    def search(self):
        try:
            key = int(self.entry.get())
            self.entry.delete(0, tk.END)
            self.update_result_label("Search result: " + self.tree.search(key).string if self.tree.search(key)
                                     else 'Not found')
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")

    def update_result_label(self, text):
        self.result_label.config(text=text)

    def update_tree_display(self):
        result = self.tree.inorder_traversal()
        self.tree_display.config(text="Binary Search Tree: " + str(result))


if __name__ == "__main__":
    root = tk.Tk()
    app = TreeGUI(root)
    root.mainloop()
