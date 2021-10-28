# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

# Применил метод ввода, что показывали на уроке
fields = ('first_name', 'last_name', 'year_birth', 'city_residence', 'email', 'phone')
data = {field: input(f'Введите значение поля {field} ') for field in fields}


def func1(f_name, l_name, year, city, email, phone):
    print(f_name, l_name, year, city, email, phone)


func1(data['first_name'], data['last_name'], data['year_birth'], data['city_residence'], data['email'], data['phone'])
