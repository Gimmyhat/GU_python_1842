from functools import wraps


def type_logger(func):

    @wraps(func)
    def wrapper(*args):
        arg = func(*args)
        for item in args:
            print(f'{func.__name__}({item}: {type(item)})')
        return arg

    return wrapper


@type_logger
def calc_cube(x, y):
    return x ** y


if __name__ == '__main__':
    a = calc_cube(5.2, 7)
    print(a)
