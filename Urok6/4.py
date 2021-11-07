# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
# скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
# результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direct):
        self.direct = direct
        print(f'Машина {self.name} повернула {self.direct}')

    def show_speed(self):
        print(f'Родитель: Текущая скорость автомобиля {self.name} около {self.speed}')


class TownCar(Car):
    def tw_car(self):
        print('Я TownCar')

    def show_speed(self):
        if self.speed > 60:
            print(f'Потомок: Текущая скорость автомобиля {self.name} превышена {self.speed}')
        else:
            Car.show_speed(self)


class SportCar(Car):
    def sp_car(self):
        print('Я SportCar')


class WorkCar(Car):
    def wr_car(self):
        print('Я WorkCar')

    def show_speed(self):
        if self.speed > 40:
            print(f'Потомок: Текущая скорость автомобиля {self.name} превышена {self.speed}')
        else:
            Car.show_speed(self)


class PoliceCar(Car):
    def cop_car(self):
        print('Я PoliceCar')


lada = TownCar(120, 'red', 'lada', False)
lada.go()
lada.show_speed()
lada.speed = 50
lada.show_speed()

ford = WorkCar(200, 'green', 'ford', False)
ford.go()
ford.show_speed()
ford.speed = 30
ford.show_speed()
ford.turn('налево')
