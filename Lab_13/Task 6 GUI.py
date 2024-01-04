from collections import namedtuple
import random
import tkinter as tk
from tkinter import messagebox

# Створюємо іменований кортеж Athlete
Athlete = namedtuple('Athlete', ['surname', 'birth_year', 'total_score', 'city'])

# Генеруємо 7 випадкових спортсменів
athletes = [Athlete(f'Athlete{i}', 1980 + i, random.randint(1, 100), f'City{i}') for i in range(7)]
print(athletes[0][1])


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


def create_athlete():
    # Створюємо нового спортсмена з даними, введеними користувачем
    athlete = Athlete(surname_var.get(), int(birth_year_var.get()), int(total_score_var.get()), city_var.get())

    # Додаємо нового спортсмена до списку
    athletes.append(athlete)

    # Очищуємо вхідні поля
    surname_var.set('')
    birth_year_var.set('')
    total_score_var.set('')
    city_var.set('')


# Створюємо головне вікно Tkinter
root = tk.Tk()

# Створюємо вхідні поля для даних спортсмена
surname_var = tk.StringVar()
birth_year_var = tk.StringVar()
total_score_var = tk.StringVar()
city_var = tk.StringVar()

surname_entry = tk.Entry(root, textvariable=surname_var)
birth_year_entry = tk.Entry(root, textvariable=birth_year_var)
total_score_entry = tk.Entry(root, textvariable=total_score_var)
city_entry = tk.Entry(root, textvariable=city_var)

# Створюємо мітки для вхідних полів
surname_label = tk.Label(root, text="Прізвище:")
birth_year_label = tk.Label(root, text="Рік народження:")
total_score_label = tk.Label(root, text="Загальний бал:")
city_label = tk.Label(root, text="Місто:")

# Створюємо кнопку для створення нового спортсмена
btn_create_athlete = tk.Button(root, text="Створити спортсмена", command=create_athlete)

# Розташовуємо мітки та вхідні поля на екрані
surname_label.pack()
surname_entry.pack()
birth_year_label.pack()
birth_year_entry.pack()
total_score_label.pack()
total_score_entry.pack()
city_label.pack()
city_entry.pack()
btn_create_athlete.pack()

# Створюємо кнопки для запуску функцій good_athletes() та update_scores()
btn_good_athletes = tk.Button(root, text="Показати найкращих спортсменів", command=good_athletes)
btn_update_scores = tk.Button(root, text="Оновити бали", command=update_scores)

# Розташовуємо кнопки на екрані
btn_good_athletes.pack()
btn_update_scores.pack()

# Запускаємо головний цикл Tkinter
root.mainloop()
