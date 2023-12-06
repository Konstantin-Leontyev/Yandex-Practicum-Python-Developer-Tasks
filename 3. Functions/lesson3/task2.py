resorts = ['Сочи', 'курорты Краснодарского Края', 'Санкт-Петербург', 'Карелию']


def choose_vacation_place(resorts):
    for resort in resorts:
        if resort == 'Сочи':
            return resort


resort = choose_vacation_place(resorts)
print('Поехали в ' + resort)
