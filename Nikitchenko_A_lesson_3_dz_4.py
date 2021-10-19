from Nikitchenko_A_lesson_3_dz_3 import thesaurus  # сосздание словаря по именам


def thesaurus_adv(*names):  # создание вложенного словаря с ключами из первых букв фамилии
    list_of_names = list(names)
    keys_last_name = sorted(tuple(set(map(lambda x: x[x.find(' ')+1], list_of_names))))
    values = []
    my_dict = {}
    for item in keys_last_name:
        values.append(sorted(list(filter(lambda x: x[x.find(' ')+1] == item, list_of_names))))
        for item2 in values:
            my_dict[item] = thesaurus(*item2)
    return my_dict
temp_dict = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Игорь Сергеев", "Алексей Сабутин")

print(temp_dict)