"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных
экземпляров. Проверьте корректность полученного результата.
"""


class CustomComplex:

    def __init__(self, a, b):
        self.real = a
        self.image = b
        self.z = f'{a} + {b}j'

    def __str__(self):
        return self.z

    def __add__(self, other):
        return f'{self.real + other.real} + {self.image + other.image}j'

    def __mul__(self, other):
        return f'{self.real * other.real - self.image * other.image}' \
               f' + {self.image * other.real + self.real * other.image}j'


if __name__ == '__main__':
    z1 = CustomComplex(1, 1)
    z2 = CustomComplex(1, 4)

    print(z1)  # 1 + 1j
    print(z1 + z2)  # 2 + 5j
    print(z1 * z2)  # -3 + 5j
