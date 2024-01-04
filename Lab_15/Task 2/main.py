import tkinter as tk


class GUI:
    def __init__(self, _root):
        self.l1 = None
        self.l2 = None
        self.l3 = None
        self.modified_list = None
        self.root = _root
        self.root.title("App")

        self.read_data_button = tk.Button(self.root, text='Read Data', command=self.read_list_from_file_click)
        self.read_data_button.pack()

        self.l1_label = tk.Label(self.root, text='List 1:')
        self.l1_label.pack()

        self.l1_data_label = tk.Label(self.root)
        self.l1_data_label.pack()

        self.l2_label = tk.Label(self.root, text='List 2:')
        self.l2_label.pack()

        self.l2_data_label = tk.Label(self.root)
        self.l2_data_label.pack()

        self.l3_label = tk.Label(self.root, text='List 3:')
        self.l3_label.pack()

        self.l3_data_label = tk.Label(self.root)
        self.l3_data_label.pack()

        self.write_data_button = tk.Button(self.root, text='Write Data', command=self.save_to_file)
        self.write_data_button.pack()

        self.l1_modified_label = tk.Label(self.root, text='Modified L1:')
        self.l1_modified_label.pack()

        self.l1_modified_data_label = tk.Label(self.root)
        self.l1_modified_data_label.pack()

    def read_list_from_file_click(self):
        self.l1 = read_list_from_file('L1.txt')
        self.l2 = read_list_from_file('L2.txt')
        self.l3 = read_list_from_file('L3.txt')

        self.modified_list = replace_list(self.l1, self.l2, self.l3)

        self.l1_data_label.config(text=' '.join(self.l1))
        self.l2_data_label.config(text=' '.join(self.l2))
        self.l3_data_label.config(text=' '.join(self.l3))

    def save_to_file(self):
        with open('modified_L1.txt', 'w') as file:
            for i in range(0, len(self.modified_list), 7):
                file.write(' '.join(map(str, self.modified_list[i:i + 7])) + '\n')

        self.l1_modified_data_label.config(text=' '.join(self.modified_list))


def read_list_from_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        return [x for x in data.strip().split()]


def replace_list(L1, L2, L3):
    result = L1.copy()
    pos = contains(L2, L1)
    if pos:
        result[pos[0]:pos[1]] = L3
    return result


def contains(small, big):
    for i in range(len(big) - len(small) + 1):
        for j in range(len(small)):
            if big[i + j] != small[j]:
                break
        else:
            return i, i + len(small)
    return False


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
