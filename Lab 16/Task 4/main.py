import tkinter as tk
from tkinter import ttk
from graph import Graph
from tkinter import messagebox


class GraphInputApp:
    def __init__(self, root):
        self.adjacency_list = dict()
        self.graph = None
        self.root = root
        self.root.title("Graph Input GUI")

        style = ttk.Style()
        style.theme_use('clam')

        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10)

        ttk.Label(input_frame, text="Vertex").grid(row=0, column=0)
        ttk.Label(input_frame, text="Neighbors").grid(row=0, column=1)

        self.vertex_entry = ttk.Entry(input_frame)
        self.neighbors_entry = ttk.Entry(input_frame)

        self.vertex_entry.grid(row=1, column=0)
        self.neighbors_entry.grid(row=1, column=1)

        add_button = ttk.Button(input_frame, text="Add Edge", command=self.add_edge)
        add_button.grid(row=1, column=2)

        output_frame = ttk.Frame(self.root)
        output_frame.pack(pady=10)

        self.output_text = tk.Text(output_frame, wrap=tk.WORD, width=40, height=10)
        self.output_text.grid(row=0, column=0, padx=10)

        show_button = ttk.Button(output_frame, text="Show Graph Info", command=self.display_graph_info)
        show_button.grid(row=1, column=0)

        self.table1 = ttk.Treeview(root)
        self.table1.heading("#0", text="Row/Col")
        self.table1.column("#0", width=80, anchor='center', stretch=False)

        self.table2 = ttk.Treeview(root)
        self.table2.heading("#0", text="Row/Col")
        self.table2.column("#0", width=80, anchor='center', stretch=False)

    def add_edge(self):
        vertex = self.vertex_entry.get()
        neighbors = self.neighbors_entry.get().split(',')
        neighbors = [neighbor.strip() for neighbor in neighbors]
        if len(neighbors) != len(set(neighbors)):
            messagebox.showerror('identical vertices', 'Vertices should be unique')
            return

        self.adjacency_list[vertex] = neighbors
        self.graph = Graph(self.adjacency_list)

        self.vertex_entry.delete(0, tk.END)
        self.neighbors_entry.delete(0, tk.END)

        self.display_graph_info()

    def display_graph_info(self):
        self.output_text.delete(1.0, tk.END)

        self.output_text.insert(tk.END, "Adjacency List:\n")
        for vertex, neighbors in self.graph.adjacency_list.items():
            self.output_text.insert(tk.END, f"{vertex}: {neighbors}\n")

        self.output_text.insert(tk.END, "\nEdge List:\n")
        for edge in self.graph.edges_list:
            self.output_text.insert(tk.END, f"{edge[0]} - {edge[1]}\n")

        self.table1.pack_forget()
        self.table1.delete(*self.table1.get_children())
        self.table1['columns'] = self.graph.vertices
        self.table1['height'] = len(self.graph.vertices)

        for heading, row in zip(self.table1['columns'], self.graph.adjacency_matrix):
            self.table1.column(heading, width=50, anchor=tk.CENTER, stretch=tk.NO)
            self.table1.heading(heading, text=heading)
            self.table1.insert('', tk.END, values=row, text=heading)

        self.table1.pack()

        self.table2.pack_forget()
        self.table2.delete(*self.table2.get_children())
        self.table2['columns'] = tuple(range(len(self.graph.edges_list)))
        self.table2['height'] = len(self.graph.vertices)

        for col_heading in self.table2['columns']:
            self.table2.column(col_heading, width=50, anchor=tk.CENTER, stretch=tk.NO)
            self.table2.heading(col_heading, text=col_heading)

        for row_heading, row in zip(self.graph.vertices, self.graph.incidence_matrix):
            self.table2.insert('', tk.END, values=row, text=row_heading)

        self.table2.pack()


if __name__ == '__main__':
    root = tk.Tk()
    app = GraphInputApp(root)
    root.mainloop()
