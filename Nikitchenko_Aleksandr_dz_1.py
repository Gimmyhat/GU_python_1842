def seconds_convertor(sec):
    day = sec // 86400
    hour = (sec % 86400) // 3600
    minute = (sec % 3600) // 60
    second = (sec % 60)
    return [day, hour, minute, second]

while True:
    try:
        time_digit = seconds_convertor(int(input('Введите количество секунд (q - выход): ')))
        time_text = ['дн', 'час', 'мин', 'сек']
        while time_digit[0] == 0:
            time_digit.pop(0) and time_text.pop(0)
        for i in range(len(time_digit)):
            print(time_digit[i], time_text[i], end=' ')
        print()
    except:
        print('Выход')
        break

