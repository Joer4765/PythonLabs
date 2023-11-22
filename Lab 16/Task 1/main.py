from queue import LifoQueue
import tkinter as tk


class GUI:
    def __init__(self, _root):
        self.formula = None
        self.root = _root
        self.root.title("App")

        self.read_data_button = tk.Button(self.root, text='Read Data', command=self.read_from_file_click)
        self.read_data_button.pack()

        self.formula_label = tk.Label(self.root, text='Formula:')
        self.formula_label.pack()

        self.formula_data_label = tk.Label(self.root)
        self.formula_data_label.pack()

        self.process_data_button = tk.Button(self.root, text='Process Data', command=self.is_brackets_balanced_click)
        self.process_data_button.pack()

        self.result_label = tk.Label(self.root, text='Result:')
        self.result_label.pack()

        self.result_data_label = tk.Label(self.root)
        self.result_data_label.pack()

    def read_from_file_click(self):
        with open('formula.txt', 'r') as file:
            self.formula = file.read()
        self.formula_data_label.config(text=self.formula)

    def is_brackets_balanced_click(self):
        stack = LifoQueue()
        brackets_i = []
        is_brackets_balanced = True
        for i, c in enumerate(self.formula):
            if c == '(':
                stack.put(i)
            elif c == ')':
                if not stack.empty():
                    brackets_i.append((stack.get(), i))
                else:
                    is_brackets_balanced = False
                    break

        if not stack.empty():
            is_brackets_balanced = False

        if is_brackets_balanced:
            self.result_label.config(text=str(brackets_i))

        else:
            self.result_label.config(text='Brackets arent balanced')


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
