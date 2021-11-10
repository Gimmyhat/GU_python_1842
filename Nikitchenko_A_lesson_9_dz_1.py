import time


class TrafficLight:
    __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}

    def running(self):
        for color, period in self.__color.items():
            print(color)
            time.sleep(period)


traffic_light = TrafficLight()
for _ in range(2):
    traffic_light.running()
