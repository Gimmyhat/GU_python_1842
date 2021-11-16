import time


class Date:

    def __init__(self, param):
        self.param = param

    @classmethod
    def str_to_digits(cls, param):
        return tuple(map(int, param.split('-')))

    @staticmethod
    def validate(date):
        try:
            time.strptime(date, '%d-%m-%Y')
        except ValueError:
            print('Invalid date!')
            return False
        else:
            return True


print(Date.str_to_digits('17-15-2021'))  # (17, 15, 2021)
print((Date.validate('29-02-2021')))  # Invalid date! -> False
print(Date.validate('01-10-2020'))  # True
