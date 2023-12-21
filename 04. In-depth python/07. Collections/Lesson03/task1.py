def assess_yield(number_of_plants, average_weight):
    # Ваш код здесь
    total_weight = number_of_plants * (average_weight / 1000)
    if total_weight > 100:
        rating = 'Ожидается отличный урожай.'
    elif 50 < total_weight <= 100:
        rating = 'Ожидается хороший урожай.'
    elif 0 < total_weight <= 50:
        rating = 'Урожай будет так себе.'
    else:
        rating = 'Урожая не будет.'
    return total_weight, rating


# Пример вызова функции
total_weight, rating = assess_yield(50, 200)
print(total_weight, 'кг.', rating)
