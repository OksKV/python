# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию  type() для проверки типа.

new_list = [1, 3.8, True, 'some string', ['kitty', 16], (67, 'name', 1.1), None, {32, 1, 3}]
for element in new_list:
    print(type(element))