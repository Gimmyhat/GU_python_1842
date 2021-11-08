import yaml
import os


def recursive_list(array, level, lst):  # преобразует структуру из config.yaml в список с путями
    if isinstance(array, dict):
        for key, value in array.items():
            lst.append(f'{level}\\{key}')
            recursive_list(value, f'{level}\\{key}', lst)
    elif isinstance(array, list):
        for item in array:
            if isinstance(item, dict):
                for key, value in item.items():
                    lst.append(f'{level}\\{key}')
                    recursive_list(value, f'{level}\\{key}', lst)
            else:
                 lst.append(f'{level}\\{item}')
    return lst


def get_structure(lst):  # создает структуру из пакок и файлов по шаблону
    def_path = os.getcwd()  # текущая рабочая директория
    for item in lst:
        path = os.path.normpath(def_path + item)
        if not os.path.exists(path):  # если path(папка или файл) не существует
            if os.path.splitext(item)[1] == '':
                os.mkdir(path)  # создает директорию
            else:
                with open(path, 'w', encoding='utf-8') as f:
                    f.writable()  # создает файл



if __name__ == '__main__':
    with open('config.yaml') as f:
        templates: dict = yaml.safe_load(f)

    get_structure(recursive_list(templates, '', []))
