
from math import sqrt
from typing import Optional


def add_numbers(term1: int, term2: int) -> int:
    return term1 + term2


def calculate_square_root(number: float) -> float:
    return sqrt(number)


def calc(your_number: float) -> Optional[str]:

    if your_number <= 0:
        return None
    root = calculate_square_root(your_number)
    return (f'Мы вычислили квадратный корень из введённого вами числа. '
            f'Это будет: {root}')


num1: int = 10
num2: int = 5

print('Сумма чисел:', add_numbers(num1, num2))

print(calc(25.5))
