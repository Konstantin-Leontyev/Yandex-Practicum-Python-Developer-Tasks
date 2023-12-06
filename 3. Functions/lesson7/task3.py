# Функция для вычисления площади куба.
def calc_cube_area(side):
    # Формулу для вычисления площади одной грани куба Афанасий написал:
    one_face = side * side

    # Вычислите полную площадь куба: у него шесть одинаковых граней.
    cube_area = one_face * 6

    # Удалите многоточие и допишите функцию так,
    # чтобы она возвращала полную площадь куба
    return cube_area


# Присвойте переменной one_cube_area значение,
# которое вернёт функция calc_cube_area() с аргументом 3:
# 3 метра - это длина ребра куба.
one_cube_area = calc_cube_area(3)

# Вычислите общую площадь стекла, необходимого
# для строительства 8 кубов,
# и сохраните это значение в переменную full_area
full_area = one_cube_area * 8

print('Необходимая площадь стекла для 8 кубов, кв.м:', full_area)
