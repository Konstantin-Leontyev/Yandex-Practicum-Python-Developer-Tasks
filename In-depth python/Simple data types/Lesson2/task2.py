# Получаем данные в секундах
response = 424562

# Переведите полученное значение в необходимые единицы измерения
days = response // 86400
hours = (response - (days * 86400)) // 3600
minutes = (response - (days * 86400) - (hours * 3600)) // 60
seconds = response - (days * 86400) - (hours * 3600) - (minutes * 60)

print(response, 'секунд - это')
print('Дней:', days)
print('Часов:', hours)
print('Минут:', minutes)
print('Секунд:', seconds)
