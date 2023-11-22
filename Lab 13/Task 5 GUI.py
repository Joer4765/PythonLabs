import tkinter as tk
from tkinter import messagebox


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task 5 GUI")
        self.geometry("525x350")

        tk.Label(self, text="Прізвище студента:").grid(row=0, column=0, padx=20, pady=(20, 0))
        self.student_name_entry = tk.Entry(self, width=30)
        self.student_name_entry.grid(row=0, column=1, padx=20, pady=(20, 0))

        tk.Label(self, text="Оцінки за домашні завдання (через кому):").grid(row=1, column=0, padx=20)
        self.homework_scores_entry = tk.Entry(self, width=30)
        self.homework_scores_entry.grid(row=1, column=1, padx=20)

        tk.Label(self, text="Оцінка за іспит:").grid(row=2, column=0, padx=20)
        self.exam_score_entry = tk.Entry(self, width=30)
        self.exam_score_entry.grid(row=2, column=1, padx=20)

        calculate_button = tk.Button(self, text="Розрахувати оцінку", command=self.calculate_score)
        calculate_button.grid(row=3, column=0, columnspan=2, padx=20, pady=(20, 0))

        self.result_label = tk.Label(self, text="", anchor="w", justify="left", wraplength=480)
        self.result_label.grid(row=4, column=0, columnspan=2, padx=20, pady=(20, 0))

    def calculate_score(self):
        student_name = self.student_name_entry.get()
        homework_scores_text = self.homework_scores_entry.get()
        exam_score_text = self.exam_score_entry.get()

        try:
            homework_scores = list(map(int, homework_scores_text.split(',')))
            exam_score = int(exam_score_text)

            if len(homework_scores) != 6:
                raise ValueError("Уведіть рівно 6 оцінок через кому.")

            homework_average = sum(homework_scores) / 6
            final_grade = int(0.4 * homework_average + 0.6 * exam_score)

            result_text = f"Студент {student_name} – ваша підсумкова оцінка за іспит {final_grade}"
            self.result_label.config(text=result_text)

        except ValueError as e:
            messagebox.showerror("Помилка", str(e))


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()

