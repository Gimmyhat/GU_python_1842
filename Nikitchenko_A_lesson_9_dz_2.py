class Road:

    def __init__(self, length=None, width=None):
        self._length = length
        self._width = width

    def calculate(self):
        return self._length * self._width * 25 * 5


total_weight = Road(20, 5000)
print(f'{total_weight.calculate()/1000:.0f} т')
