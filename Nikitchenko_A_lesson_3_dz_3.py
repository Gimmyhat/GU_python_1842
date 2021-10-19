def thesaurus(*names):
    list_of_names = list(names)
    keys = sorted(tuple(set(map(lambda x: x[0], list_of_names))))
    values = []
    my_dict = {}
    for item in keys:
        values.append(list(filter(lambda x: x[0] == item, list_of_names)))
    my_dict.update(zip(keys, values))
    return my_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
