def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def add_zero(str):
    if len(str) == 1:
        str = '0' + str
    elif int(str) < 10:
        str = str[0] + '0' + str[1]
    return str


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(my_list)):
    if is_int(my_list[i]):  # если строка является числом
        my_list[i] = add_zero(my_list[i])  # дополняем нулём до двух целочисленных разрядов
print(my_list)

# добавляем кавычки между всеми значениями списка, являющимися цифрами
k = 0
for i in range(len(my_list)):
    if is_int(my_list[i+k]):  # если строка является числом
        my_list.insert(i + k, '"')
        k += 1
        my_list.insert(i + k + 1, '"')
        k += 1

# распечатываем кавычки без пробелов для чисел, остальные значения печатаем с пробелами
for i in range(len(my_list)):
    if my_list[i] == '"' and is_int(my_list[i+1]) or is_int(my_list[i]):
        print(my_list[i], end='')
    else:
        print(my_list[i], end=' ')


