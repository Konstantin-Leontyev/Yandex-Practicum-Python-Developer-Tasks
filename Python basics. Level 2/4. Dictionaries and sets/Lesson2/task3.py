def get_together_games(anfisa_games, alisa_games):
    # Напишите здесь код функции для поиска пересечений
    return anfisa_games.intersection(alisa_games)

anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]
# Вызовите функцию со списками игр в качестве параметров
together_games = get_together_games(set(anfisa_games), set(alisa_games))
# Напечатайте итоговый перечень игр в цикле
for game in together_games:
    print('👾', game)
