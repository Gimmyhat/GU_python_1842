# дни, часы, минуты - в секундах
minute_in_sec = 60
hour_in_sec = minute_in_sec * 60
day_in_sec = hour_in_sec * 24
# условие завершения цикла - ввод нуля
condition = True
while condition:
    duration = int(input("Введите промежуток времени в секундах (для выхода нажмите '0'): "))
    day = duration // day_in_sec
    hour = duration % day_in_sec // hour_in_sec
    minute = duration % day_in_sec % hour_in_sec // minute_in_sec
    second = duration % day_in_sec % hour_in_sec % minute_in_sec
    if duration == 0:
        condition = False
    elif duration >= day_in_sec:
        print(f'{day} дн {hour} час {minute} мин {second} сек')
    elif duration >= hour_in_sec:
        print(f'{hour} час {minute} мин {second} сек')
    elif duration >= minute_in_sec:
        print(f'{minute} мин {second} сек')
    else:
        print(f'{second} сек')

