
def formula(rate, hours, bonus):
    """
    Высчитывает зарплату за количество отработанных часов
    """
    salary = hours * rate
    return salary + salary * (bonus / 100)


if __name__ == '__main__':
    print(formula(20, 5, 15))

