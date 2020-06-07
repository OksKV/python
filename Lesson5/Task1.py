# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

edit_file = open('new_file', 'a+')
while True:
    new_line = input('Введите новые данные')
    if not new_line == '':
        edit_file.write(new_line + '\n')
    else:
        break
edit_file.seek(0)
data = edit_file.read()
edit_file.close()
print(data)

