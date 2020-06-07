# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time


class TrafficLight:
    __attr = 'color'

    def running(self, color1='red', color2='yellow', color3='green'):
        self.color1 = color1
        print(f'Traffic light switched to {self.color1}')
        time.sleep(7)
        self.color2 = color2
        print(f'Traffic light switched to {self.color2}')
        time.sleep(2)
        self.color3 = color3
        print(f'Traffic light switched to {self.color3}')
        time.sleep(5)


runner = TrafficLight()
runner.running()
