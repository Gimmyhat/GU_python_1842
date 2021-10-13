for i in range(1, 101):
    if i % 10 == 1 and i // 10 != 1:
        print(f'{i} процент')
    elif i % 10 in (2, 3, 4) and i // 10 != 1:
        print(f'{i} процента')
    else:
        print(f'{i} процентов')
