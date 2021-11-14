def if_error(val, cls):
    if not isinstance(val, cls):
        raise TypeError


class Cell:

    def __init__(self, amount: int):
        if_error(amount, int)
        self.amount = amount

    def __add__(self, other):
        if_error(other, Cell)
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        if_error(other, Cell)
        sub = self.amount - other.amount
        return Cell(sub) if sub > 0 else print(f'{self.amount} < {other.amount}, вычитание невозможно')

    def __mul__(self, other):
        if_error(other, Cell)
        return Cell(self.amount * other.amount)

    def __floordiv__(self, other):
        if_error(other, Cell)
        return Cell(self.amount // other.amount)

    def __truediv__(self, other):
        if_error(other, Cell)
        return Cell(round(self.amount / other.amount))

    def make_order(self, num):
        return '\n'.join('*' * num for _ in range(self.amount // num)) + '\n' + '*' * (self.amount % num)


y = Cell(47)
x = Cell(7)
try:
    z = y + x
    print(z.amount)
    z = y - x
    print(z.amount)
    z = x * y
    print(z.amount)
    z = y / x
    print(z.amount)
    z = y // x
    print(z.amount)
    print(y.make_order(10))
except Exception as e:
    print(e)
