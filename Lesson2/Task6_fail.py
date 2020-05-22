# Реализовать структуру данных  « Товары » . Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента  — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.


def add_item():
    titles = ['name', 'price', 'quantity', 'unit']
    request = (input("Введите через пробел: 1. Название товара, 2. Цену($), 3. Количество 4. Ед. измерения")).split()
    return dict(zip(titles, request))  # or new_item = {key: value for key, value in zip(titles, request)}


def create_list():
    new_item = []
    created_list = []
    num_item = 1
    while True:
        respond = (input("Вы хотите добавить новый товар? Введите да/нет")).lower()
        if respond == 'да':
            new_item.append(num_item)
            new_item.append(add_item())
            num_item += 1
            created_list.append(tuple(new_item))
            print(f'Ваш список продуктов: {created_list}')
        elif respond == 'нет':
            print('До новых встреч!')
            break
        else:
            print('Введено неверное значение')
            create_list()


print('Давайте сформируем список покупок!')
create_list()

