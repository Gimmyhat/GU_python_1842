class ErrorFind(Exception):
    """ Ошибка - данное оборудование отсутвует в отделе """
    pass


class ErrorDept(Exception):
    """ Ошибка в названии отдела """
    def __str__(self):
        return f'Такой отдел не существует!'


class Equipment:
    """ Базовый класс для всей оргтехники """
    product_id = 1

    # в конструкторе каждому экземпляру присваивается уникальный ID
    def __init__(self, model_name):
        self.model_name = model_name
        self.product_id = f'{self.__class__.__name__}_{Equipment.product_id:03}'
        Equipment.product_id += 1


class Printer(Equipment):

    def __init__(self, model_name, print_speed):
        super().__init__(model_name)
        self.print_speed = print_speed


class Scanner(Equipment):

    def __init__(self, model_name, dpi):
        super().__init__(model_name)
        self.dpi = dpi


class Copier(Equipment):
    def __init__(self, model_name, speed_copy):
        super().__init__(model_name)
        self.speed_copy = speed_copy


class Warehouse:
    """ Базовый класс для склада"""
    __main_db = {'Склад': {},
                 'Ресепш': {},
                 'Бухгалтерия': {}}
    base_dept = 'Склад'

    # добавление техники в базу даных (первоначально все поступает в подразделение "Склад")
    @classmethod
    def add(cls, unit, dept=base_dept):
        try:
            # проверка на корректный ввод названия отдела
            if dept not in Warehouse.__main_db:
                raise ErrorDept
            # создаем ключ в базе для выбранного отдела в зависимости от типа техники
            key = f'{unit.__class__.__name__.lower()}s'
            Warehouse.__main_db.setdefault(dept).setdefault(key)
            # добавляем девайс в список
            if Warehouse.__main_db[dept][key] is None:
                Warehouse.__main_db[dept][key] = [unit]
            else:
                Warehouse.__main_db[dept][key].append(unit)
        except ErrorDept as ex:
            print(ex)

    # движение техники между подразделениями
    @classmethod
    def transfer(cls, unit, dept_out, dept_in):
        try:
            if (dept_in or dept_out) not in Warehouse.__main_db:
                raise ErrorDept
            # поиск по названию в базе
            for value in Warehouse.__main_db[dept_out].values():
                # преобразование списка девайсов в список названий девайсов
                value_names = [x.model_name for x in value]
                # находим индекс в списке и переносим из одного отдела в другой
                if unit in value_names:
                    idx = value_names.index(unit)
                    Warehouse.add(value.pop(idx), dept_in)
                    break
            else:
                # если в выбраном отделе указанный девайс отсутствует, то ошибка
                raise ErrorFind
        except ErrorDept as ex:
            print(ex)
        except ErrorFind:
            print(f'"{unit}" в отделе "{dept_out}" не найден!')

    # вывод на печать базы даных
    @classmethod
    def print_db(cls):
        total = 0
        for key, value in Warehouse.__main_db.items():
            print(f'{key}:')
            for k, v in value.items():
                print(f'    {k} - {len(v)} шт: {[x.model_name for x in v]}')
                total += len(v)
            print("-" * 50)
        print(f'Общее количество техники на предприятии: {total}')


def main():
    printer1 = Printer('Xerox-5040', 30)
    printer2 = Printer('Canon-1016', 50)
    printer3 = Printer('Canon-2020', 15)
    printer4 = Printer('Epson F10', 25)
    scanner1 = Scanner('Epson S111', 600)
    copier1 = Copier('Xerox ZPT1200', 60)
    copier2 = Copier('Xerox ZPT1000', 45)

    Warehouse.add(printer1)
    Warehouse.add(printer2)
    Warehouse.add(scanner1)
    Warehouse.add(copier1)
    Warehouse.add(copier2)

    Warehouse.transfer('Canon-1016', 'Склад', 'Ресепш')  # переносит принтер со Склада в отдел Ресепш
    Warehouse.transfer('Canon-1016', 'Склад', 'Ресепш')  # ошибка - "Canon-1016" в отделе "Склад" не найден!
    Warehouse.transfer('Xerox-5040', 'Склад', 'БухгЛатерия')  # Выдает ошибку - "Такой отдел не существует!"
    Warehouse.transfer('Xerox ZPT1000', 'Склад', 'Бухгалтерия')  # переносит сканер со Склада в отдел Бухгалтерия
    Warehouse.transfer('Xerox ZPT1000', 'Бухгалтерия', 'Склад')  # возврат на Склад
    Warehouse.transfer('Xerox ZPT1200', 'Склад', 'Бухгалтерия')
    Warehouse.print_db()  # выводит на печать текущее местоположение оргтехники


if __name__ == '__main__':
    main()
