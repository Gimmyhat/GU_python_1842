# разбиение числа на составляющие его цифры
def digits_recursive(n, digits=[]):
    return digits_recursive(n // 10, [n % 10] + digits) if n else digits or [0]

# суммирование цифр числа
def sum_digits(number):
    return sum(digits_recursive(number))

# суммирование числа из списка, которые делятся на 7 без остатка
def sum_div7(user_list):
    sum_num_div_7 = 0
    for num in user_list:
        if sum_digits(num) % 7 == 0:
            sum_num_div_7 += num
    return sum_num_div_7

# создание списка, состоящего из кубов нечётных чисел от 1 до 1000
my_list = [i ** 3 for i in range(1000) if i % 2 != 0]

print(sum_div7(my_list))
print(sum_div7([i+17 for i in my_list]))
