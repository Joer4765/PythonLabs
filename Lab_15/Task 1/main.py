import tkinter as tk
from dll_gui import DllGUI
from sll_gui import SllGUI


class LinkedListApp:
    def __init__(self, _root):
        self.root = _root
        self.root.title("Linked List App")

        self.singly_list_button = tk.Button(self.root, text="Work with Singly Linked List", command=SllGUI)
        self.singly_list_button.pack(pady=10)

        self.doubly_list_button = tk.Button(self.root, text="Work with Doubly Linked List", command=DllGUI)
        self.doubly_list_button.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = LinkedListApp(root)
    root.mainloop()
