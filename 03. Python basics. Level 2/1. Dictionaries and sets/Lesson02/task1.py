# В данном случае мы принудительно задаем тип данных для параметров функций.
# Указывая что функция принимает на вход два множества all_cities и used_cities
# При таком подходе среда разработки будет знать с объектом какого типа
# осуществляются действия внутри функции.
# Это позволит использовать подсказки при точечном обращении к методам множества
def print_valid_cities(all_cities: set, used_cities: set):
    # Вместо этого многоточия напишите код функции, она должна
    # принимать и обрабатывать аргументы all_cities и used_cities,
    # а затем печатать результат в нужном формате
    unused_cities = all_cities.difference(used_cities)

    for city in unused_cities:
        print(city)


all_cities = {
    'Абакан',
    'Астрахань',
    'Бобруйск',
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк',
    'Новосибирск'
}

used_cities = {
    'Калуга',
    'Абакан',
    'Новосибирск'
}

print_valid_cities(all_cities, used_cities)
