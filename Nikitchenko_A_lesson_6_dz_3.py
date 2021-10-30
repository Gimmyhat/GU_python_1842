import random


def generate_users(n=5):  # Генерируем список ФИО
    last_name = ['Федоров', 'Сидоров', 'Петренко', 'Смолин', 'Артемьев']
    first_name = ['Александр', 'Иван', 'Сергей', 'Петр', 'Андрей']
    middle_name = ['Иванович', 'Петрович', 'Алексеевич', 'Юрьевич', 'Сергеевич']
    return [f"{random.choice(last_name)}, {random.choice(first_name)}, {random.choice(middle_name)}\n" for _ in range(n)]


def generate_hobby(n=5):  # Генерируем список хобби
    hobby = ['горные лыжи', 'беговые лыжи', 'футбол', 'теннис', 'баскетбол',
             'бег', 'велосипед', 'мотоцикл', 'рыбалка', 'альпинизм']
    return [(', '.join(random.sample(hobby, random.randint(1, 3))))+'\n' for _ in range(n)]



if __name__ == '__main__':

    # Запись в файл 'users.csv'
    with open('users.csv', 'w', encoding='utf-8') as f:
        f.writelines(generate_users(4))

    # Запись данных в файл 'hobby.csv'
    with open('hobby.csv', 'w', encoding='utf-8') as f:
        f.writelines(generate_hobby(3))

    with open('users.csv', 'r', encoding='utf-8') as f:
        l_users = [line.strip().replace(',', ' ') for line in f]

    with open('hobby.csv', 'r', encoding='utf-8') as f:
        l_hobby = [line.strip() for line in f]

    diff = len(l_users) - len(l_hobby)
    if diff >= 0:
        l_hobby.extend([None]*diff)
        dictionary = dict(zip(l_users, l_hobby))
        print(dictionary)
    elif diff < 0:
        print('1')

