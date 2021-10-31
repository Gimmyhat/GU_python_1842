import random
import sys


def generate_users(n=5):  # Генерируем список ФИО
    last_name = ['Федоров', 'Сидоров', 'Петренко', 'Смолин', 'Артемьев']
    first_name = ['Александр', 'Иван', 'Сергей', 'Петр', 'Андрей']
    middle_name = ['Иванович', 'Петрович', 'Алексеевич', 'Юрьевич', 'Сергеевич']
    return [f"{random.choice(last_name)}, {random.choice(first_name)}, {random.choice(middle_name)}\n" for _ in
            range(n)]


def generate_hobby(n=5):  # Генерируем список хобби
    hobby = ['горные лыжи', 'беговые лыжи', 'футбол', 'теннис', 'баскетбол',
             'бег', 'велосипед', 'мотоцикл', 'рыбалка', 'альпинизм']
    return [(', '.join(random.sample(hobby, random.randint(1, 3)))) + '\n' for _ in range(n)]


def read_write(file, user_list=None, oper='r'):  # Функция записи/чтения файла
    with open(file, oper, encoding='utf-8') as f:
        if oper == 'w':
            f.writelines(user_list)
        elif oper == 'r':
            return [line.strip() for line in f]


if __name__ == '__main__':
    n_users = 7
    n_hobby = 5
    try:
        if sys.argv[1:]:
            file_users = sys.argv[1]
            file_hobby = sys.argv[2]
            file_result = sys.argv[3]
        else:
            file_users = 'users.csv'
            file_hobby = 'hobby.csv'
            file_result = 'users_hobby.txt'
        # Запись в файл
        read_write(file_users, generate_users(n_users), 'w')
        read_write(file_hobby, generate_hobby(n_hobby), 'w')
        # Чтение из файла в список
        l_users = read_write(file_users)
        l_hobby = read_write(file_hobby)
        diff = len(l_users) - len(l_hobby)
        # Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None
        if diff >= 0:
            users_hobby = []
            l_hobby.extend([None] * diff)
            for x, y in zip(l_users, l_hobby):
                users_hobby.append(f'{x}: {y}\n')
            read_write(file_result, users_hobby, 'w')
        # Если наоборот — выходим из скрипта с кодом «1»
        elif diff < 0:
            print('1')
    except IndexError:
        print(f'Аргументов должно быть 3')
    print('Задача выполнена!')
