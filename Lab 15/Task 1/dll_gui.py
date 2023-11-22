import tkinter as tk
from dll import DoublyLinkedList
from tkinter import messagebox


class DllGUI(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("DLL App")

        self.linked_list = DoublyLinkedList()

        self.ins = tk.Frame(self)
        self.ins.grid(row=0, column=0)

        self.data_label = tk.Label(self.ins, text='Address book (for inserting):')
        self.data_label.grid(row=0, column=0)

        self.data_entry = tk.Entry(self.ins)
        self.data_entry.grid(row=1, column=0)

        self.pos_label = tk.Label(self.ins, text='pos:')
        self.pos_label.grid(row=0, column=1)

        self.pos_entry = tk.Entry(self.ins, width=3)
        self.pos_entry.grid(row=1, column=1)

        self.op = tk.Frame(self)
        self.op.grid(row=1, column=0)

        self.input1_label = tk.Label(self.op, text='Input1 (for another ops):')
        self.input1_label.pack()

        # Entry field for user input
        self.input1_entry = tk.Entry(self.op)
        self.input1_entry.pack()

        self.input2_label = tk.Label(self.op, text='Input2 (for another ops):')
        self.input2_label.pack()

        # Entry field for user input
        self.input2_entry = tk.Entry(self.op)
        self.input2_entry.pack()

        # Buttons for different operations

        self.display_button = tk.Button(self.op, text="Display List", command=self.display_list)
        self.display_button.pack()

        self.size_button = tk.Button(self.op, text="List Size", command=self.size)
        self.size_button.pack()

        self.is_empty_button = tk.Button(self.op, text="Is List Empty", command=self.is_empty)
        self.is_empty_button.pack()

        self.insert_beginning_button = tk.Button(self.op, text="Insert at Beginning", command=self.insert_at_beginning)
        self.insert_beginning_button.pack()

        self.insert_end_button = tk.Button(self.op, text="Insert at End", command=self.insert_at_end)
        self.insert_end_button.pack()

        self.insert_end_button = tk.Button(self.op, text="Insert at Index", command=self.insert_at_pos)
        self.insert_end_button.pack()

        self.remove_all_button = tk.Button(self.op, text="Remove All Elements", command=self.remove_all)
        self.remove_all_button.pack()

        self.remove_at_index_button = tk.Button(self.op, text="Remove At Index", command=self.remove_at_index)
        self.remove_at_index_button.pack()

        self.remove_value_button = tk.Button(self.op, text="Remove Value", command=self.remove_value)
        self.remove_value_button.pack()

        self.remove_values_button = tk.Button(self.op, text="Remove Values", command=self.remove_values)
        self.remove_values_button.pack()

        self.edit_button = tk.Button(self.op, text="Edit Value", command=self.edit)
        self.edit_button.pack()

        self.replace_all_button = tk.Button(self.op, text="Replace All Values", command=self.replace_all)
        self.replace_all_button.pack()

        self.search_button = tk.Button(self.op, text="Search By Index", command=self.search)
        self.search_button.pack()

        self.sort_button = tk.Button(self.op, text="Sort List", command=self.sort_list)
        self.sort_button.pack()

        self.save_to_file_button = tk.Button(self.op, text="Save To File", command=self.save_to_file)
        self.save_to_file_button.pack()

        self.load_from_file_button = tk.Button(self.op, text="Load From File", command=self.load_from_file)
        self.load_from_file_button.pack()

        self.out = tk.Frame(self)
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
        self.update_output(str(self.linked_list))

    def size(self):
        self.update_output(self.linked_list.size)

    def is_empty(self):
        self.update_output('List is empty' if self.linked_list.is_empty() else 'List is not empty')

    def insert_at_beginning(self):
        data = self.data_entry.get()
        if data:
            self.linked_list.insert_at_beginning(data)
            self.data_entry.delete(0, 'end')
            self.display_list()

    def insert_at_end(self):
        data = self.data_entry.get()
        if data:
            self.linked_list.insert_at_end(data)
            self.data_entry.delete(0, 'end')
            self.display_list()

    def insert_at_pos(self):
        data = self.data_entry.get()
        pos = self.pos_entry.get()
        if data and pos:
            self.linked_list.insert_at_position(data=data, position=int(pos))
            self.data_entry.delete(0, 'end')
            self.input1_entry.delete(0, 'end')
            self.display_list()

    def remove_all(self):
        self.linked_list.remove_all()
        self.display_list()

    def remove_at_index(self):
        data = self.input1_entry.get()
        if data:
            self.linked_list.remove_at_index(int(data))
            self.input1_entry.delete(0, 'end')
            self.display_list()

    def remove_value(self):
        data = self.input1_entry.get()
        if data:
            self.linked_list.remove_value(data)
            self.input1_entry.delete(0, 'end')
            self.display_list()

    def remove_values(self):
        data = self.input1_entry.get()
        if data:
            self.linked_list.remove_values(list(data.split()))
            self.input1_entry.delete(0, 'end')
            self.display_list()

    def edit(self):
        old = self.input1_entry.get()
        new = self.input2_entry.get()
        if old and new:
            self.linked_list.edit(old, new)
            self.input1_entry.delete(0, 'end')
            self.input2_entry.delete(0, 'end')
            self.display_list()

    def replace_all(self):
        old = self.input1_entry.get()
        new = self.input2_entry.get()
        if old and new:
            self.linked_list.replace_all(old, new)
            self.input1_entry.delete(0, 'end')
            self.input2_entry.delete(0, 'end')
            self.display_list()

    def search(self):
        data = self.input1_entry.get()
        if data:
            result = self.linked_list.search(int(data))
            self.input1_entry.delete(0, 'end')
            self.update_output(result)

    def sort_list(self):
        self.linked_list.sort()
        self.display_list()

    def save_to_file(self):
        self.linked_list.save_to_file('dll.txt')
        messagebox.showinfo('', 'Saved successfully')

    def load_from_file(self):
        self.linked_list.load_from_file('dll.txt')
        self.display_list()
