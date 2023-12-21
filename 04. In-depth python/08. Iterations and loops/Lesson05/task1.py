# Пригодится для наполнения списков!
import random

# 1. Создание списка списков:
...
harvest = [[random.randint(5, 20) for _ in range(3)] for _ in range(3)]  # Примените list comprehension.


# 2. Функция для подсчёта общего урожая:
def total_harvest(harvest):
    result = 0
    for garden_bed in harvest:
        result += sum(garden_bed)
    return result


# 3. Функция для подсчёта среднего урожая с каждого участка:
def average_harvest_per_plot(harvest):
    return [sum(garden_bed) / 3 for garden_bed in harvest]


# Вывод результатов
print('Урожай с каждой грядки на каждом участке:', harvest)
print('Общий урожай со всех участков:', total_harvest(harvest))
print('Средний урожай с каждого участка:', average_harvest_per_plot(harvest))
