class Matrix:
    def __init__(self, *args):
        self.list = []
        self.list.extend(args)

    def __str__(self):
        return str(['\t'.join(map(str, i)) for i in self.list])


    # def __add__(self, other):
    #     for row in self.list:
    #         for i in row:
    #             Matrix(self.list[i] + other.list[i])

mtrx1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
mtrx2 = Matrix([3, 2, 1], [6, 5, 4], [9, 8, 7])
print(mtrx1)
print(mtrx2)
