class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return print(f'{self.name} go forward!')

    def stop(self):
        return print(f'{self.name} stopped!')

    def turn(self, direction):
        return print(f'{self.name} turn {direction}')

    def show_speed(self):
        return print(f'speed car = {self.speed} km/h')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return print(f'Attention! Over speed!')
        else:
            return print(f'speed car = {self.speed} km/h')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return print(f'Attention! Over speed!')
        else:
            return print(f'speed car = {self.speed} km/h')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


car1 = TownCar(70, 'Green', 'Lada', False)

car1.show_speed()
car1.turn('left')
car1.go()

car2 = SportCar(220, 'Red', 'Audi', False)

print(car2.name)
car2.show_speed()
car2.stop()

car3 = WorkCar(45, 'Gray', 'KAMAZ', False)

print(car3.color)
car3.show_speed()
print(car3.is_police)

car4 = PoliceCar(180, 'White', 'BMW', True)

print(car4.is_police)
car4.go()
car4.show_speed()

