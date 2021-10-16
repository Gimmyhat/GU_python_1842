def print_price(lst, space):
    print(space.join([f'{str(float(item)).split(".")[0]} руб {str(float(item)).split(".")[1]:02} коп' for item in lst]))


# список с ценами
price = [57.8, 46.51, 97, 48, 54.44, 70.1, 90, 111.12, 65.01, 7.2, 59, 78, 91.5, 78, 15.7]

print_price(price, ', ')  # печатаем список цен в формате <r> руб <kk>
print_price(sorted(price), '\n')  # вывод списка с ценами, отсортированными по возрастанию
print(price)  # доказательство, что объект списка после сортировки остался тот же
price_sort_z_a = sorted(price, reverse=True)  # новый список цен по убыванию
print_price(sorted(sorted(price, reverse=True)[:5]), '\n')  # вывод пяти самых дорогих товара по возрастанию
