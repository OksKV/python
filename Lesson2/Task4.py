# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

phrase = input("Please insert a phrase")
new_phrase = phrase.split()

for ind, word in enumerate(new_phrase, 1):
    print(ind, word[:11])