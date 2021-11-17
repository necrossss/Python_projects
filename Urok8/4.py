# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

class Store:
    print('Склад')


class Office_Equipment:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def run(self):
        print('Это оргтехника')


class Printer(Office_Equipment):
    def __init__(self, color, weight, print_speed):
        super().__init__(color, weight)
        self.print_speed = print_speed

    def run(self):
        print('Это принтер!')
        print(f'Характеристики: цвет - {self.color} вес - {self.weight} скорость печати - {self.print_speed}')


class Scanner(Office_Equipment):
    def __init__(self, color, weight, scanner_type):
        super().__init__(color, weight)
        self.scanner_type = scanner_type

    def run(self):
        print('Это сканер!')
        print(f'Характеристики: цвет - {self.color} вес - {self.weight} тип сканера - {self.scanner_type}')


class Xerox(Office_Equipment):
    def __init__(self, color, weight, print_speed, mode):
        super().__init__(color, weight)
        self.print_speed = print_speed
        self.mode = mode

    def run(self):
        print('Это ксерокс!')
        print(
            f'Характеристики: цвет - {self.color} вес - {self.weight} скорость печати - {self.print_speed} режим - {self.mode}')


printer = Printer('black', 3, 20)
scaner = Scanner('white', 2, 'планшетный')
xerox = Xerox('red', 20, 30, 'auto')

printer.run()
scaner.run()
xerox.run()
