# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


# Вариант 1.
text = ''


def int_func(word):
    word = list(word)
    word[0] = word[0].upper()
    word = ''.join(map(str, word))
    return word


while True:
    try:
        text = input('Введите строку слов в нижнем регистре: ')
        text.encode("iso-8859-1")
        break
    except:
        print('Используйте только латинские буквы!')
        continue

lst = text.split()
for ls in lst:
    print(int_func(ls), end=' ')

'''
# Вариант 2. Коротко =))
def int_func(word):
    print(word.title())
int_func('text word str')
'''
