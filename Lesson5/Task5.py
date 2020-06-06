# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('Task5.txt', 'w+') as file:
    file.write('1 4 56 23 8 5 12')
    file.seek(0)
    reader = file.read()
total_sum = sum(map(int, reader.split()))
print(total_sum)