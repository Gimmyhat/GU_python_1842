import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    line_index = 1
    for line in f:
        if len(sys.argv[1:]) == 0:  # просто запуск скрипта — выводить все записи;
            print(line.strip())
        elif len(sys.argv[1:]) == 1:  # выводить все записи с номера, равного этому числу, до конца
            if int(sys.argv[1]) <= line_index:
                print(line.strip())
        elif len(sys.argv[1:]) == 2:  # выводить записи, ограниченные первым и вторым номерами включительно
            if int(sys.argv[1]) <= line_index <= int(sys.argv[2]):
                print(line.strip())
        line_index += 1



