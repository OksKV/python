# 1. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# 2. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.

some_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list1 = [i for i in some_list[1:] if i > some_list[some_list.index(i) - 1]]

new_list2 = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]

print(new_list1)
print(new_list2)
