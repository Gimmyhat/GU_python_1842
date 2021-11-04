from pathlib import Path
from pprint import pprint

sort_size = {
    100: [0, []],
    1000: [0, []],
    10000: [0, []],
    100000: [0, []],
    1000000: [0, []]
}

# Задаю директорию для обработки
root_dir = Path.cwd() / 'my_project'
# Создаю список всех файлов в дереве каталогов заданной дирректории в формате ['.exp', size]
files = [[f.suffix, f.stat().st_size] for f in root_dir.rglob('*.*')]
for file in files:
    start = -1
    for key in sort_size.keys():
        if start < file[1] <= key:
            sort_size[key][0] += 1  # подсчет файлов для каждой категории
            sort_size[key][1].append(file[0])  # список расширений файлов, попавших в категорию
            start = key
        sort_size[key][1] = list(set(sort_size[key][1]))  # оставляю только уникальные расширения
for key in sort_size.keys():
    sort_size[key] = tuple(sort_size[key])  # преобразую список в кортеж

pprint(sort_size)
