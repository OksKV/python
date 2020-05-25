# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# Method 1


def my_func1(x, y):
    return x ** y


print(my_func1(2, -2))


# Method 2


def my_func2(x, y):
    step = 0
    total = 1
    while step < abs(y):
        step += 1
        total *= x
    return 1 / total


print(my_func2(2, -2))
