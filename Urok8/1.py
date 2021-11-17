# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    dd = 0
    mm = 0
    yy = 0

    def __init__(self, date):
        self.date = date

    @classmethod
    def convert_int(cls, str_date):
        print(str_date)
        my_list = str_date.split('-')
        my_list = [int(item) for item in my_list]
        cls.dd = my_list[0]
        cls.mm = my_list[1]
        cls.yy = my_list[2]

    @staticmethod
    def check():
        if Date.dd <= 0 or Date.dd > 31:
            print(f'Число "{Date.dd}" выходит за пределы от 1 до 31')
        if Date.mm <= 0 or Date.mm > 12:
            print(f'Число "{Date.mm}" выходит за пределы от 1 до 12')
        if Date.yy < 1970 or Date.yy > 2100:
            print(f'Число "{Date.yy}" выходит за пределы от 1970 до 2100')


Date.convert_int('33-10-2021')
Date.check()
