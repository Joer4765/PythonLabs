from collections import namedtuple
import random
import tkinter as tk
from tkinter import messagebox

# Створюємо іменований кортеж Athlete
Athlete = namedtuple('Athlete', ['surname', 'birth_year', 'total_score', 'city'])

# Генеруємо 7 випадкових спортсменів
athletes = [Athlete(f'Athlete{i}', 1980 + i, random.randint(1, 100), f'City{i}') for i in range(7)]


def good_athletes():
    # Обчислюємо середній бал
    avg_score = sum(a.total_score for a in athletes) / len(athletes)

    # Формуємо список спортсменів, у яких загальний бал вищий за середній
    good_athletes = [a for a in athletes if a.total_score > avg_score]

    # Виводимо повідомлення
    messagebox.showinfo("Результат",
                        f'Спортсмени {", ".join(a.surname for a in good_athletes)} в цьому турнірі найкращі!')


def update_scores():
    global athletes
    # Задаємо нове значення поля кортежу «загальний бал за змагання» для всіх спортсменів
    athletes = [a._replace(total_score=random.randint(1, 100)) for a in athletes]


# Створюємо головне вікно Tkinter
root = tk.Tk()

# Створюємо кнопки для запуску функцій good_athletes() та update_scores()
btn_good_athletes = tk.Button(root, text="Показати найкращих спортсменів", command=good_athletes)
btn_update_scores = tk.Button(root, text="Оновити бали", command=update_scores)

# Розташовуємо кнопки на екрані
btn_good_athletes.pack()
btn_update_scores.pack()

# Запускаємо головний цикл Tkinter
root.mainloop()

class Product:

    Athlete = namedtuple('Athlete', ['surname', 'birth_year', 'total_score', 'city'])

    def __init__(self, surname, birth_year, total_score, city):

        self.data = Athlete()

    def get_all_values(self):
        return self.data

    def get_value(self, index):
        return self.data[index]