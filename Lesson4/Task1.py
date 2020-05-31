# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from Lesson4.my_funcs import formula

employers = {'Ben': [250, 160], 'Mary': [300, 100],
             'Sam': [550, 180], 'Nina': [200, 80]}  # value[0]- rate; value[1] - hours


def salary_counter():
    bonus = int(input("введите размер премии в этом месяце (в процентах от зарплаты): "))
    for emp in employers:
        print(f'For employee {emp} the salary in this month will be '
              f'{formula(employers[emp][0], employers[emp][1], bonus)}$')


salary_counter()
