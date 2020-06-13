class Cell:

    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return Cell(self.cells - other.cells)
        else:
            return 'Разность меньше нуля'

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        try:
            return Cell(self.cells // other.cells)
        except ZeroDivisionError:
            return 'Деление невозможно'

    def make_order(self, num):
        for i in range(self.cells // num):
            print('*' * num)
        print('*' * (self.cells % num))

    def __str__(self):
        return str(self.cells)


cell1 = Cell(12)
cell2 = Cell(13)
print(cell1 + cell2)
cell1.make_order(4)
