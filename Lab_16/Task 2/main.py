import tkinter as tk
from deque import Deque

class DequeGUI:
    def __init__(self, _root):
        self.root = root
        self.root.title("Deque App")

        self.deque = Deque()

        self.ins = tk.Frame(self.root)
        self.ins.grid(row=0, column=0)

        self.data_label = tk.Label(self.ins, text='Input:')
        self.data_label.grid(row=0, column=0)

        self.data_entry = tk.Entry(self.ins)
        self.data_entry.grid(row=1, column=0)

        self.op = tk.Frame(self.root)
        self.op.grid(row=1, column=0)

        # Buttons for different operations

        self.display_button = tk.Button(self.op, text="Display Deque", command=self.display_list)
        self.display_button.pack()

        self.size_button = tk.Button(self.op, text="Deque Size", command=self.size)
        self.size_button.pack()

        self.is_empty_button = tk.Button(self.op, text="Is Deque Empty", command=self.is_empty)
        self.is_empty_button.pack()

        self.push_front_button = tk.Button(self.op, text="Push Front", command=self.push_front)
        self.push_front_button.pack()

        self.push_back_button = tk.Button(self.op, text="Push Back", command=self.push_back)
        self.push_back_button.pack()

        self.pop_front_button = tk.Button(self.op, text="Pop Front", command=self.pop_front)
        self.pop_front_button.pack()

        self.pop_back_button = tk.Button(self.op, text="Pop Back", command=self.pop_back)
        self.pop_back_button.pack()

        self.front_button = tk.Button(self.op, text="Front", command=self.front)
        self.front_button.pack()

        self.back_button = tk.Button(self.op, text="Back", command=self.back)
        self.back_button.pack()

        self.back_button = tk.Button(self.op, text="Clear", command=self.clear)
        self.back_button.pack()

        self.out = tk.Frame(self.root)
        self.out.grid(row=0, column=1, sticky=tk.NW, rowspan=2)

        self.output_label = tk.Label(self.out, text='Output:')
        self.output_label.grid(row=0, column=0, sticky=tk.NW)

        self.output_text = tk.Text(self.out, width=40, height=10)
        self.output_text.grid(row=1, column=0, sticky=tk.NW)
        self.output_text.configure(state="disabled")

    def update_output(self, data):
        self.output_text.configure(state="normal")
        self.output_text.delete('1.0', 'end')
        self.output_text.insert('end', data)
        self.output_text.configure(state="disabled")

    def display_list(self):
        self.update_output(str(self.deque))

    def size(self):
        self.update_output(self.deque.size)

    def is_empty(self):
        self.update_output('List is empty' if self.deque.is_empty() else 'List is not empty')

    def push_front(self):
        data = self.data_entry.get()
        if data:
            self.deque.push_front(data)
            self.data_entry.delete(0, 'end')
            self.display_list()

    def push_back(self):
        data = self.data_entry.get()
        if data:
            self.deque.push_back(data)
            self.data_entry.delete(0, 'end')
            self.display_list()

    def clear(self):
        self.deque.clear()
        self.display_list()

    def pop_front(self):
        data = '' if self.deque.pop_back() is None else self.deque.pop_front()
        self.update_output(data)

    def pop_back(self):
        data = '' if self.deque.pop_back() is None else self.deque.pop_back()
        self.update_output(data)

    def front(self):
        data = self.deque.front()
        self.update_output(data)

    def back(self):
        data = self.deque.back()
        self.update_output(data)


if __name__ == "__main__":
    root = tk.Tk()
    app = DequeGUI(root)
    root.mainloop()