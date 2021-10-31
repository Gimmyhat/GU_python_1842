import fileinput
import sys


def replace_in_file(file, row, new_text):
    with fileinput.input(file, inplace=True) as f:
        index = 1
        for line in f:
            search_text = line if int(row) == index else 'xxx'
            new_line = line.replace(search_text.strip(), new_text)
            print(new_line, end='')
            index += 1


def row_count(file):
    with open(file) as f:
        return sum(1 for _ in f)


if __name__ == '__main__':
    name_file = 'bakery.csv'
    if int(sys.argv[1]) > row_count(name_file):
        print('Введенный номер записи не существует!')
    else:
        replace_in_file(name_file, sys.argv[1], sys.argv[2])
