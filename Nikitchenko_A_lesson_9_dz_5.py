class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        return print('Рисует ручка')


class Pencil(Stationery):

    def draw(self):
        return print('Рисует карандаш')


class Handle(Stationery):

    def draw(self):
        return print('Рисует маркер')


pen1 = Pen('ручка')
pen1.draw()

pencil1 = Pencil('карандаш')
pencil1.draw()

handle1 = Handle('маркер')
handle1.draw()
print(handle1.title)
