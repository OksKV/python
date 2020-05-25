# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(some_string):
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    new_string = ''
    for letter in some_string:
        if letter in alphabet:
            new_string += letter
    else:
        print('Must be latin letters')
    print(new_string.title())


int_func(input('Please insert a word or a phrase divided by blank spaces'))
