# Из модуля decimal импортируйте тип данных Decimal и параметр getcontext.
# Из модуля math импортируйте константу "пи".
from decimal import Decimal, getcontext
from math import pi

# Установите необходимую точность для вычислений.
getcontext().prec = 10

# Приведите константу "пи" к типу Decimal.
# Помните, что Decimal() принимает строку, а константа "пи" - это число.
PI = Decimal(str(pi))


# Объявите функцию ellipse_area() с двумя параметрами.
def ellipse_area(semimajor_axis, semiminor_axis):
    return PI * semimajor_axis * semiminor_axis


# Объявите три переменные типа Decimal -
# они должны хранить длины полуосей эллипса и глубину пруда.
semimajor_axis = Decimal('2.5')
semiminor_axis = Decimal('1.75')
depth = Decimal('0.35')

# Вызовите функцию ellipse_area(), в аргументах передайте длины полуосей эллипса.
area = ellipse_area(semimajor_axis, semiminor_axis)

# Вычислите объём пруда: площадь * глубина.
pond_volume = area * depth

print(f'Площадь эллипса: {area} кв.м.',
      f'Объем воды для наполнения пруда: {pond_volume} куб.м.',
      sep='\n')
