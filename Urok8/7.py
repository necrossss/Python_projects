# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class Compx:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        return ("{0} ({1} {2} {3}{4})".format("Комплексное число : ", self.real, "+", self.imag, "j"))

    def read_data(self):
        self.real = input("Введите вещественную часть :")
        self.imag = input("Введите мнимую часть :")

    def __add__(self, other):
        return Compx(int(self.real) + int(other.real), int(self.imag) + int(other.imag))

    def __mul__(self, other):
        return Compx(int(self.real) * int(other.real) - int(self.imag) * int(other.imag),
                     int(self.real) * int(other.imag) + int(self.imag) * int(other.real))
        # (a1*a2 - b1*b2) + (a1*b2 + b1*a2)j


a = Compx()
b = Compx()
print('Введите первое комплексное число: ')
a.read_data()
print('Введите второе комплексное число: ')
b.read_data()
print(a)
print(b)
print('Сумма - ', a + b)
print('Умножение - ', a * b)
