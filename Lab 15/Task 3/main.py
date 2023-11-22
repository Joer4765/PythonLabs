import tkinter as tk
from cll import CircularLinkedList
from re import findall


class CllGUI:
    def __init__(self, _root, lst):
        self.root = _root
        self.root.title("App")
        self.lst = lst

        self.in_label = tk.Label(self.root, text='Footballers Surnames')
        self.in_data_entry = tk.Entry(self.root)
        self.process_data_button = tk.Button(self.root, text="Process Data", command=self.process_data_button_click)
        self.in_data_label = tk.Label(self.root, wraplength=200, justify='left')

        self.group1_label = tk.Label(self.root, text='Footballers Group 1')
        self.group1_data_label = tk.Label(self.root, wraplength=200, justify='left')

        self.group2_label = tk.Label(self.root, text='Footballers Group 2')
        self.group2_data_label = tk.Label(self.root, wraplength=200, justify='left')

        self.in_label.pack()
        self.in_data_entry.pack()
        self.in_data_label.pack()
        self.process_data_button.pack()
        self.group1_label.pack()
        self.group1_data_label.pack()
        self.group2_label.pack()
        self.group2_data_label.pack()

    def process_data_button_click(self):

        cll = CircularLinkedList()

        for el in findall(string=self.in_data_entry.get(), pattern=r'\".+\"'):
            cll.add_end(el)

        cll1 = CircularLinkedList()
        size = 0
        i = 0
        el = cll.last.next
        while size < 10:
            i += 1
            if i % 12 == 0:
                cll1.add_end(el.data)
                cll.delete_node(el.data)
                size += 1
            el = el.next

        cll2 = CircularLinkedList()

        cll_el = cll.last.next
        while cll_el:

            new_el = True
            cll1_el = cll1.last.next

            while cll1_el:

                if cll_el.data == cll1_el.data:
                    new_el = False
                    break

                cll1_el = cll1_el.next
                if cll1_el == cll1.last.next:
                    break

            if new_el:
                cll2.add_end(cll_el.data)

            cll_el = cll_el.next
            if cll_el == cll.last.next:
                break

        self.group1_data_label.config(text=str(cll1))
        self.group2_data_label.config(text=str(cll2))


# Driver Code
if __name__ == "__main__":

    footballer_surnames = [
        "Ronaldo",
        "Messi",
        "Neymar",
        "Pogba",
        "Salah",
        "Modric",
        "Griezmann",
        "Kane",
        "Lewandowski",
        "Sterling",
        "Ramos",
        "Aguero",
        "Cavani",
        "Iniesta",
        "Ter Stegen",
        "Alaba",
        "Isco",
        "Kroos",
        "Hazard",
        "Suarez"
    ]

    root = tk.Tk()
    app = CllGUI(root, footballer_surnames)
    root.mainloop()
