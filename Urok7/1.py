# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, list, name='result'):
        self.list = list
        self.name = name

    def __str__(self):
        for n in self.list:
            print(n)
        return f'Матрица {self.name}\n'

    def __add__(self, other):
        return Matrix(
            [[self.list[i][j] + other.list[i][j] for j in range(len(self.list[0]))] for i in range(len(self.list))])


m_a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'A')
print(m_a)
m_b = Matrix([[0, 2, 5], [0, 2, 3], [0, 1, 0]], 'B')
print(m_b)

print(m_a + m_b)
