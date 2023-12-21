from random import randint

# Начальная температура чая
current_temperature = 85

# Объявите цикл while
while current_temperature > 60:
    # В теле цикла получите случайное значение температуры,
    # на которое остыл чай в этой итерации (в диапазоне от 1 до 3).
    rand_temperature = randint(1, 3)
    # Уменьшите температуру чая на полученное значение.
    current_temperature -= rand_temperature
    # Напечатайте нужные сообщения.
    print('Прошла минута.')
    print(f'Чай остыл ещё на {rand_temperature} °C. Текущая температура: {current_temperature} °C')

# Напечатайте сообщение, которое должно быть выведено после завершения цикла.
print('Время пить чай!')
