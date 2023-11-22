from enum import Enum


class Cities(Enum):
    Київ = 1
    Львів = 2
    Одеса = 3
    Харків = 4
    Дніпро = 5
    Запоріжжя = 6
    Чернігів = 7
    Івано_Франківськ = 8
    Тернопіль = 9
    Черкаси = 10

    def output_element(self):
        print(f'Ім’я: {self.name}, Значення: {self.value}')

    def output_element_name(self):
        print(f'Ім’я: {self.name}')

    def output_element_value(self):
        print(f'Значення: {self.value}')


# Вивести всі елементи enum
for city in Cities:
    city.output_element()

print()

# Вивести тільки імена
for city in Cities:
    city.output_element_name()

print()

# Вивести тільки значення
for city in Cities:
    city.output_element_value()
