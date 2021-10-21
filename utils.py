import requests
from decimal import Decimal
import sys
import datetime as DT


def currency_rates(currency):
    currency = currency.upper()
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url).text
    start = response.find("Date")
    date = DT.datetime.strptime(response[start+6:start+16], '%d.%m.%Y').date()
    if response.find(currency) <= 0:
        return None
    else:
        start = response.find(currency)
        end = response.find('</Value>', start)
        char_code = response[end-7:end].replace (',', ".")
    return currency, Decimal(char_code).quantize(Decimal("1.0000")), date

