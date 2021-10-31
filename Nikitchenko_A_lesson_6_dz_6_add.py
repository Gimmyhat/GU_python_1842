import sys

with open('bakery.csv', 'a+', encoding='utf-8') as f:
    f.write(sys.argv[1]+'\n')
    sales_amount = 0
    f.seek(0)
    for line in f:
        sales_amount += float(line)  # выводит сумму продаж
    print(f'Сумма продаж: {sales_amount:.2f}')
