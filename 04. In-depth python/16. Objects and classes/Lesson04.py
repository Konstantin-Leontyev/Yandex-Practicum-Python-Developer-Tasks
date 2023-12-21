class Employee:
    # Вместо инструкции pass напишите свой код.
    vacation_days = 28

    def __init__(self, first_name_value, second_name_value, gender_value):
        self.first_name = first_name_value
        self.second_name = second_name_value
        self.gender = gender_value

    def __repr__(self):
        return (f'Имя: {self.first_name}, '
                f'Фамилия: {self.second_name}, '
                f'Пол: {self.gender}, '
                f'Отпускных дней в году: {self.vacation_days}.')


# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee(first_name_value='Роберт',
                     second_name_value='Крузо',
                     gender_value='м')

employee2 = Employee(first_name_value='Роберт',
                     second_name_value='Крузо',
                     gender_value='м')

print(employee2)
print(employee2)
