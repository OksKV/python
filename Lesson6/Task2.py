# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_cover(self, thickness=3, mass=20):
        return int((self._length * self._width * thickness * mass) / 1000)

main_road = Road(3500, 10)
print(f"Total amount of asphalt for main road is {main_road.road_cover()} tons.")