# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def my_func(num1, num2, num3):
    new_list = []
    new_list.append(int(num1))
    new_list.append(int(num2))
    new_list.append(int(num3))
    new_list.remove(min(new_list))
    print(sum(new_list))


my_func('10', 8, 5)
