import tkinter as tk
from tkinter import messagebox


class Publication:
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

    def show(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPublisher: {self.publisher}"

    def __del__(self):
        messagebox.showinfo('Cleaning', "Publication object deleted")


class Book(Publication):
    def __init__(self, title, author, publisher, pages):
        super().__init__(title, author, publisher)
        self.pages = pages

    def show(self):
        return super().show() + f"\nPages: {self.pages}"


class Journal(Publication):
    def __init__(self, title, author, publisher, issue):
        super().__init__(title, author, publisher)
        self.issue = issue

    def show(self):
        return super().show() + f"\nIssue: {self.issue}"


class Textbook(Book):
    def __init__(self, title, author, publisher, pages, subject):
        super().__init__(title, author, publisher, pages)
        self.subject = subject

    def show(self):
        return super().show() + f"\nSubject: {self.subject}"


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Publication Demo")

        self.title_label = tk.Label(self.window, text="Title")
        self.title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(self.window)
        self.title_entry.grid(row=0, column=1)

        self.author_label = tk.Label(self.window, text="Author")
        self.author_label.grid(row=1, column=0)
        self.author_entry = tk.Entry(self.window)
        self.author_entry.grid(row=1, column=1)

        self.publisher_label = tk.Label(self.window, text="Publisher")
        self.publisher_label.grid(row=2, column=0)
        self.publisher_entry = tk.Entry(self.window)
        self.publisher_entry.grid(row=2, column=1)

        self.pages_label = tk.Label(self.window, text="Pages")
        self.pages_label.grid(row=3, column=0)
        self.pages_entry = tk.Entry(self.window)
        self.pages_entry.grid(row=3, column=1)

        self.issue_label = tk.Label(self.window, text="Issue")
        self.issue_label.grid(row=4, column=0)
        self.issue_entry = tk.Entry(self.window)
        self.issue_entry.grid(row=4, column=1)

        self.subject_label = tk.Label(self.window, text="Subject")
        self.subject_label.grid(row=5, column=0)
        self.subject_entry = tk.Entry(self.window)
        self.subject_entry.grid(row=5, column=1)

        self.publication_type_label = tk.Label(self.window, text="Publication Type")
        self.publication_type_label.grid(row=6, column=0)
        self.publication_type = tk.StringVar(self.window)
        self.publication_type.set("Publication")
        self.publication_type_menu = tk.OptionMenu(self.window, self.publication_type, "Publication", "Book", "Journal",
                                                   "Textbook")
        self.publication_type_menu.grid(row=6, column=1)

        self.create_button = tk.Button(self.window, text="Create", command=self.create_publication)
        self.create_button.grid(row=7, column=0)

        self.output_label = tk.Label(self.window, text="Output")
        self.output_label.grid(row=8, column=0)
        self.output_text = tk.Text(self.window, height=10, width=40)
        self.output_text.grid(row=8, column=1)

    def create_publication(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        publisher = self.publisher_entry.get()
        pages = self.pages_entry.get()
        issue = self.issue_entry.get()
        subject = self.subject_entry.get()

        if self.publication_type.get() == "Publication":
            publication = Publication(title, author, publisher)
        elif self.publication_type.get() == "Book":
            publication = Book(title, author, publisher, pages)
        elif self.publication_type.get() == "Journal":
            publication = Journal(title, author, publisher, issue)
        elif self.publication_type.get() == "Textbook":
            publication = Textbook(title, author, publisher, pages, subject)

        output = publication.show()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, output)


app = App()
app.window.mainloop()
