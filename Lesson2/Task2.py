# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию  input()

new_list = []
a = 0
user_list_len = int(input("Please insert a length of your list"))

while a < user_list_len:
    new_element = input("Please enter a new value of any type")
    new_list.append(new_element)
    a += 1
print(f'Your list is {new_list}')

if len(new_list) % 2 == 0:
    for i in range(0, len(new_list) - 1, 2):
        new_list[i], new_list[i+1] = new_list[i+1], new_list[i]
else:
    for i in range(0, len(new_list) - 2, 2):
        new_list[i], new_list[i+1] = new_list[i+1], new_list[i]
print(f'New list is {new_list}')



