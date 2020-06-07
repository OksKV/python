# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('Task4_eng.txt') as file:
    for line in file.readlines():
        new_file = open('Task4_rus.txt', 'a')
        new_file.write(line)
        new_file.close()
with open('Task4_rus.txt') as file:
    data = file.read()
print(data)
