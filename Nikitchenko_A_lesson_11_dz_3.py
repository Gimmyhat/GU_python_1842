class CustomError(ValueError):

    def __str__(self):
        return 'Неверный тип данных. Введите число!'


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def main(arr):
    while True:
        try:
            value = input('Введите число: ')
            if is_number(value):
                arr.append(value)
            elif value == 'q':
                break
            else:
                raise CustomError
        except CustomError as ex:
            print(ex)
    print(arr)


if __name__ == '__main__':
    main([])
