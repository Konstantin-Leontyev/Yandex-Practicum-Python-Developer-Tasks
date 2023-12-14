# Подключите библиотеку random и дайте ей краткое имя
import random as rand

answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']


def how_are_you():
    # Напишите ваш код здесь
    return rand.choice(answers)


print(how_are_you())
