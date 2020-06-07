# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

line_count = 0
words_count = 0
with open('new_file') as my_file:
    file_content = my_file.readlines()
    for line in file_content:
        line = line.split()
        line_count += 1
        words_count += len(line)
        print(f'В {line_count} строке слов: {len(line)}')
print(f'Всего в Вашем файле строк: {line_count}, слов: {words_count} ')
