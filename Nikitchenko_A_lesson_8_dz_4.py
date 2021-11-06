from functools import wraps


def val_checker(callback):
    def _val_checker(func):

        @wraps(func)
        def wrapper(num):
            if callback(num):
                return func(num)
            else:
                raise ValueError(f'wrong val {num}')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(-7))
