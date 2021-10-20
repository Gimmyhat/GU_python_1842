def thesaurus_adv(*names, deep_level=True):  # создание вложенного словаря с ключами из первых букв фамилии
    values = []
    my_dict = {}
    k = 0  # 0 - если нужно искать по имени, 1 - если по фамилии
    list_of_names = list(names)
    if deep_level:
        k = 1
    keys = sorted(tuple(set(map(lambda x: x[(x.find(' ')+1) * k], list_of_names))))
    for item in keys:
        values.append(sorted(list(filter(lambda x: x[(x.find(' ') + 1) * k] == item, list_of_names))))
        if deep_level:
            for item2 in values:
                my_dict[item] = thesaurus_adv(*item2, deep_level=False)
        else:
            my_dict.update(zip(keys, values))
    return my_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов",
                    "Анна Савельева", "Игорь Сергеев", "Алексей Сабутин"))
