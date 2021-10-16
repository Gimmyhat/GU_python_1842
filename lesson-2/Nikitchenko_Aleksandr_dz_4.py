employees_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                  'директор аэлита']
for i in range(len(employees_list)):
    temp_str = employees_list[i].split()  # временная строка с разбивкой элемента списка на слова
    temp_str[-1] = temp_str[-1].capitalize()
    employees_list[i] = ' '.join(temp_str)
    print(f'Привет, {employees_list[i].split()[-1]}!')