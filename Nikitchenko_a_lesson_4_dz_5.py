from utils import currency_rates
import sys

if __name__ == "__main__":
    if not sys.argv[1:]:
        list_cur = input("Введите символ(ы) валюты (через пробел): ")
        for item in list_cur.split():
            print(*currency_rates(item))
    else:
        for param in sys.argv[1:]:
            print(*currency_rates(param))