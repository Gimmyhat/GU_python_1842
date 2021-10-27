# Задача 1
def odd_nums_yield(n):
    for i in range(n + 1):
        if i % 2 != 0:
            yield i


# Задача 2
def odd_nums_compr(n):
    return (i for i in range(n + 1) if i % 2 != 0)


# Задача 3
def lists_to_tuple(l_one, l_two):
    diff = len(l_one) - len(l_two)
    l_two.extend([None for i in range(diff) if diff != 0])
    for x, y in zip(l_one, l_two):
        yield x, y


# Задача 4
def next_bigger_prev(my_list):
    return [y for x, y in zip(my_list, my_list[1:]) if y > x]


# Задача 5
def no_repeat(my_list):
    return list(filter(lambda x: my_list.count(x) == 1, my_list))


if __name__ == '__main__':
    tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
    klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
    lst_one = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    result = [12, 44, 4, 10, 78, 123]
    lst_two = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

    gen_tuple = lists_to_tuple(tutors, klasses)
    print(*gen_tuple)  # видим сгенерированный список gen_tuple
    print(*gen_tuple)  # а теперь не видим, т.к. он весь "выдохся" ))
    print(next_bigger_prev(lst_one))
    print(no_repeat(lst_two))
