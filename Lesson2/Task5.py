# Реализовать структуру  « Рейтинг » , представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [14, 9, 7, 7, 3]
while len(my_list) < 10:
    new_num = int(input("please insert a new integer"))
    for num in my_list:
        if new_num > num:
            my_list.insert(my_list.index(num), new_num)
            break
        elif new_num <= my_list[-1]:
            my_list.append(new_num)
            break
    print(my_list)
