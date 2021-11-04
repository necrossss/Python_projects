# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

count_str = 0
words = 0
try:
    with open("test.txt", "r") as f:
        for line in f.readlines():
            words = len(line.split(' '))
            print(line, end='')
            print('Слов в строке: ', words)
            count_str += 1
    print('Количество строк: ', count_str)
except FileNotFoundError:
    print('Файл не найден!')
