import requests
from decimal import Decimal
import sys
import datetime as DT


def currency_rates(currency):
    currency = currency.upper()
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url).text
    start = response.find("Date")
    end = response.find("name")
    s_date = ''.join(x for x in response[start:end] if x.isdigit())  # удаление лишних символов из даты
    date = DT.datetime.strptime(s_date, '%d%m%Y').date()
    if response.find(currency) <= 0:
        return None
    else:
        start = response.find(currency)
        end = response.find('</Value>', start)
        char_code = response[end-7:end].replace (',', ".")
    return currency, Decimal(char_code).quantize(Decimal("1.0000")), date


