# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('The car started moving')

    def stop(self):
        print('The car stopped')

    def turn(self, direction):
        self.direction = direction
        print(f'The car turned {self.direction}')

    def show_speed(self):
        print(f'Your speed is {self.speed} km/h')

class TownCar(Car):
    engine_capacity = 1.6
    transmission = 'auto'
    cabin_type = 'minivan'

    def show_speed(self):
        if self.speed > 60:
            print('Your speed is too high, please slow down!')
        else:
            print(f'Your speed is {self.speed} km/h')

class WorkCar(Car):
    engine_capacity = 1.2
    transmission = 'mechanic'
    cabin_type = 'truck'

    def show_speed(self):
        if self.speed > 40:
            print('Your speed is too high, please slow down!')
        else:
            print(f'Your speed is {self.speed} km/h')

class SportCar(Car):
    engine_capacity = 3.7
    transmission = 'mechanic'
    cabin_type = 'sport'

    def turn_turbo_mode(self):
        print('You are on Turbo Mode now! You can go 350 km//h max.')


class PoliceCar(Car):
    engine_capacity = 2.5
    transmission = 'auto'
    cabin_type = 'roadster'

    def turn_light_signal(self):
        if self.is_police == True:
            print('Police is on duty, give it a way!')
        else:
            print('The police is on watch')

car1 = TownCar(40, 'Red', 'BMW', False)
car1.show_speed()

car2 = PoliceCar(70, 'White and blue', 'Ford', True)
car2.turn_light_signal()

car3 = WorkCar(60, 'Black', 'Toyota', False)
car3.show_speed()

car4 = SportCar(100, 'Yellow', 'Lamborgini', False)
car4 = car4.turn_turbo_mode()