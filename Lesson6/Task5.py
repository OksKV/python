# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Звпуск отрисовки...')

class Pen(Stationery):

    def draw(self):
        print('Снятие колпачка')

class Pencil(Stationery):

    def draw(self):
        print('Заточка карандаша')

class Handle(Stationery):

    def draw(self):
        print('Заправка маркера')

stat1 = Pen('Ручка')
stat1.draw()

stat2 = Pencil('Карандаш')
stat2.draw()

stat3 = Handle('Маркер')
stat3.draw()