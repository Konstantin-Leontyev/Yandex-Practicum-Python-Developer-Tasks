fruit_yields = [164.8, 105.0, 124.3, 113.8]  # Урожайность, кг на дерево.
# Объявляем новый список, в него будем складывать изменённые значения.
corrected_fruit_yields = []

# Объявите цикл, в нём переберите список fruit_yields.
for fruit_yield in fruit_yields:
    # В теле цикла к каждому значению списка добавьте 1.2,
    new_value = fruit_yield + 1.2
    list.append(corrected_fruit_yields, new_value)
# затем получившееся значение сохраните в список corrected_fruit_yields.

# Чтобы увидеть, что получилось,
# напечатаем список с откорректированными значениями.
print(corrected_fruit_yields)
