# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

str = '1 2 3 4 5 6 7 8 9 10 11 12'
with open("ur5.txt", "w") as f:
    f.write(str)

with open("ur5.txt", "r") as f:
    str_2 = f.readline()
    list = str_2.split(' ')
    amount = sum(map(int, list))
print(amount)
