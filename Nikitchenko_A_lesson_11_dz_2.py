class ZeroDivError(Exception):

    def __str__(self):
        return 'Ошибка: деление на ноль!'


def div(val1, val2):
    if val2 == 0:
        raise ZeroDivError
    return val1 / val2


try:
    print(div(10, 0))
except ZeroDivError as ex:
    print(ex)

a = 10 / 5
print(a)
