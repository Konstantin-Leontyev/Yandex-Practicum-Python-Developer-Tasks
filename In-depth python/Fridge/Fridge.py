from datetime import datetime, date, timedelta
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'


# goods = {
#     # 'Пельмени Универсальные': [
#     #     {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
#     #     {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)}
#     # ],
#     # 'Вода': [{'amount': Decimal('1.5'), 'expiration_date': None}]
# }


# add(goods, 'Пельмени Универсальные', Decimal('2'), '2023-10-28')
def add(items, title, amount, expiration_date=None):
    new_item = {
        'amount': Decimal(amount),
        'expiration_date': datetime.strptime(expiration_date, DATE_FORMAT).date() if expiration_date else None
    }

    if title in items:
        items[title].append(new_item)
    else:
        items[title] = [new_item, ]


def add_by_note(items, note):
    list_str = str.split(note, ' ')
    print(list_str)
    if '-' in list_str[-1]:
        title = str.join(' ', list_str[:-2])
        good_amount = Decimal(list_str[-2])
        expiration_date = list_str[-1]
    else:
        title = str.join(' ', list_str[:-1])
        good_amount = Decimal(list_str[-1])
        expiration_date = None

    add(items, title, good_amount, expiration_date)


def find(items, needle):
    # keys_tuple = set(item.lower() for item in items)
    return [item for item in items if needle.lower() in item.lower()]


def amount(items, needle):
    good_amount = Decimal('0')

    for item in items:
        if needle.lower() in item.lower():
            for good in items[item]:
                good_amount += good['amount']

    return good_amount


def expire(items, in_advance_days=0):
    expire_list = []
    today = date.today()
    # today = date(2023, 12, 10)
    checking_date = today + timedelta(days=in_advance_days)
    for key, value in items.items():
        total_amount = Decimal('0')
        for good in value:
            if good['expiration_date']:
                if not good['expiration_date'] > checking_date:
                    total_amount += good['amount']
        if total_amount:
            temporary_tuple = key, total_amount
            expire_list.append(temporary_tuple)

    return expire_list

# add(goods, 'Пельмени Универсальные', '0.5', '2023-12-14')
# add(goods, 'Пельмени Универсальные', '2', '2023-12-14')
# add(goods, 'Вода', '1.5', '2023-12-16')
# print(goods)
# add_by_note(goods, 'Яйца гусиные 4 2023-07-15')
# add_by_note(goods, 'Яйца 1 2023-6-24')
# add_by_note(goods, 'Масло подсолнечное "Олейна" 0.5')
# print(goods)
# print(find(goods, 'йц'))
# print(amount(goods, 'яйца'))
# print(amount(goods, 'Яйца'))
# print(amount(goods, 'Пельмени Универсальные'))
# print(expire(goods))
# print(expire(goods, 1))
# Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('3'))]
# print(expire(goods, 2))
#
# goods = {
#     'Хлеб': [
#         {'amount': Decimal('1'), 'expiration_date': None},
#         {'amount': Decimal('1'), 'expiration_date': date(2023, 12, 9)}
#     ],
#     'Яйца': [
#         {'amount': Decimal('2'), 'expiration_date': date(2023, 12, 12)},
#         {'amount': Decimal('3'), 'expiration_date': date(2023, 12, 11)}
#     ],
#     'Вода': [{'amount': Decimal('100'), 'expiration_date': None}]
# }
#
# print(expire(goods))
# # Вывод: [('Хлеб', Decimal('1'))]
# print(expire(goods, 1))
# # Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('3'))]
# print(expire(goods, 2))
# # Вывод: [('Хлеб', Decimal('1')), ('Яйца', Decimal('5'))]
