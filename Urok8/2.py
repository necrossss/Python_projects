# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class Excepts(Exception):
    def __init__(self, text):
        self.txt = text


a = input('Введите делимое: ')
b = input('Введите делитель: ')
try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise Excepts('Делить на 0 нельзя!')
except ValueError:
    print('Вы ввели не число!')
except Excepts as mr:
    print(mr)
else:
    print('Ответ: ', a / b)
