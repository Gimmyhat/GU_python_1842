import requests
from decimal import Decimal
import sys
import datetime as DT


def currency_rates(currency):
    currency = currency.upper()
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url).text
    start = response.find ("Date")
    end = response.find ("name")
    date = ''.join (x for x in response[start:end] if x.isdigit ())  # удаление лишних символов из даты
    if response.find(currency) <= 0:
        return None
    else:
        start = response.find(currency)
        end = response.find('</Value>', start)
        char_code = response[end-7:end].replace (',', ".")
    return currency, Decimal(char_code).quantize(Decimal("1.0000")), date


if __name__ == "__main__":
    if not sys.argv[1:]:
        list_cur = input("Введите символ(ы) валюты (через пробел): ")
        for item in list_cur.split():
            print(*currency_rates(item))
    else:
        for param in sys.argv[1:]:
            print(*currency_rates(param))