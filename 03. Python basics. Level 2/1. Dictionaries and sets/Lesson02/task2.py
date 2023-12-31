def print_valid_cities(all_cities, used_cities):
    diff = all_cities.difference(used_cities)
    for city in diff:
        print(city)


# Вариант 1
# Посредствам цикла
# def add_cities(all_cities, new_cities):
#     # Напишите код функции
#     for city in new_cities:
#         all_cities.add(city)


# Вариант 2
# Используя методы списка

# ----ПРИМЕЧАИНЕ----
# В данном случае задействовано ключевое слово global,
# чтобы получить доступ к множеству all_cities объявленному в глобальной области видимости.
# Специальные настройки тестера Практикума, в отличие от сред разработки
# ошибки при использовании одинаковых имен параметров функции и переменных не выдает.
# Это сделано в целях упрощения понимания в рамках процесса обучения.
# Однако, на практике Вам придется работать в другой среде
# и чтобы внутри функции не происходило конфликта имен
# название принимаемого множества изменено с all_cities на all_cities_.
# Тут важно понимать, что когда мы передаем в функцию множество all_cities
# внутри функции создается копия этого множества, с которым и происходит работа.
# Результат работы функции возвращается с помощью ключевого слова return,
# которое мы рассмотрим в следующих уроках.
# В связи с тем, что Python объект-ориентированный язык, в функцию передается ссылка
# на область памяти, где лежит множество all_cities.
# Именно по этому мы можем вносить изменения в само множество all_cities.
# Но такой подход в корне не верен, и в перспективе породит множество багов кода
# по этому его лучше избегать.
# ----ПРИМЕЧАИНЕ----

# Поскольку объект new_cities имеет тип данных list (список)
# мы можем привести множество к типу данных list(all_cities_)
# и работать с методами списка.
# Раскомментируйте следующую строку для проверки любого из способов решения Варианта 2
# строка общая для всех вариантов
# def add_cities(all_cities_, new_cities):
#     # получаем доступ к множеству из глобально области видимости
#     # раскомментируйте следующую строку для проверки любого из способов решения Варианта 2
#     # строка общая для всех вариантов
#     global all_cities
#     # приводи множество к типу данных cписок list(all_cities_)
#     # раскомментируйте следующую строку для проверки любого из способов решения Варианта 2
#     # строка общая для всех вариантов
#     all_cities_ = list(all_cities_)
#     # Вариант А
#     # сложение списков
#     # раскомментируйте следующую строку для проверки варианта В
#     # all_cities_ = all_cities_ + new_cities
#
#     # Вариант Б
#     # добавление элементов списка new_cities в список all_cities_ через срез
#     # в данном случае len(all_cities_) вернет длину списка all_cities_
#     # что будет тождественно индексу последнего элемента + 1
#     # использование среза считается безопасным поскольку
#     # выход за пределы списка не порождает ошибку index out of range
#     # раскомментируйте следующую строку для проверки варианта Б
#     # all_cities_[len(all_cities_):] = new_cities
#
#     # Вариант В
#     # используя метод списка extend
#     # раскомментируйте следующую строку для проверки варианта В
#     # all_cities_.extend(new_cities)
#
#     # приводим новый список к типу данных множество set(all_cities_)
#     # раскомментируйте следующую строку для проверки любого из способов решения Варианта 2
#     all_cities = set(all_cities_)

# # Вариант 3
# # Используя метод множества update
def add_cities(all_cities, new_cities):
    # Напишите код функции
    all_cities.update(new_cities)

# При этом мы можем в принципе обойтись без функции,
# но без нее тестер яндекса не пропустит решение.
# Потому ниже пример без параметра функции all_cities
# где внутри функции вносятся изменения сразу в глобальную переменную all_cities
#
# def add_cities(new_cities):
#     # Напишите код функции
#     all_cities.update(new_cities)

# ВАЖНО! Использование глобальных переменных без крайней необходимости
# считается признаком дурного тона.
#


# Анфиса нашла названия нескольких новых городов,
# эти города нужно добавить в множество all_cities
new_cities = [
    'Екатеринбург',
    'Выборг',
    'Владивосток',
    'Казань',
    'Why',
    'Йезд'
]

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

add_cities(all_cities, new_cities)
print_valid_cities(all_cities, used_cities)
