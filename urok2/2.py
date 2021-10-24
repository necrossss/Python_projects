# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

mylist = list(input('Введите список одной строкой: '))
print(mylist)
i = 0
key = 0
last_el = 0
if len(mylist) % 2 != 0:
    last_el = mylist.pop(len(mylist) - 1)
    key = 1
for list in mylist[::2]:
    mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]
    i += 2
if key == 1:
    mylist.append(last_el)
print(mylist)
