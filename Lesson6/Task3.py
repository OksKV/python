# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'Wage': wage, 'Bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(f'Total income is {(self._income["Wage"] + self._income["Bonus"])} dollars')

worker1 = Position('Sam', 'Willson', 'Driver', 1500, 300)
worker2 = Position('Marie', 'Smith', 'Lawyer', 1700, 500)
worker3 = Position('Priscilla', 'Anderson', 'General manager', 2000, 1000)

worker1.get_full_name()
worker1.get_total_income()

worker2.get_full_name()
worker2.get_total_income()

worker3.get_full_name()
worker3.get_total_income()
