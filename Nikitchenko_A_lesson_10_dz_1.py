class Matrix:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        return '\n'.join(' '.join(str(i) for i in row) for row in self.array) + '\n'

    def __add__(self, other):
        try:
            return Matrix([list(map(sum, zip(*i))) for i in zip(self.array, other.array)])
        except AttributeError as e:
            raise e


a = Matrix([[31, 22], [37, 43], [51, 86]])
b = Matrix([[5, 41], [87, 3], [15, 25]])
print(a)
c = a + b
print(c)
print(type(c))  # <class '__main__.Matrix'>
