# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def num_division(num1, num2):
    try:
        return round(num1 / num2, 2)
    except ZeroDivisionError:
        return "Даже не  пытайся делить на ноль!"


try:
    dividend = int(input("Введите делимое"))
    divider = int(input("Введите делитель"))
    print(num_division(dividend, divider))
except ValueError:
    print("Вы ввели неверное значение! Попробуйте снова.")
