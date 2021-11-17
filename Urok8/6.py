# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
# уроках по ООП.


class Store:
    goods = {}

    # наверное нужно было как-то по-другому организовать выбор оргтехники для перевода...
    @classmethod
    def add_goods(cls, name, count):
        if name in cls.goods.keys():
            cls.goods[name] = cls.goods.get(name) + count
        else:
            cls.goods[name] = count

    def transfer(self, name, count):
        if name in self.goods.keys():
            Store.goods[name] = Store.goods.get(name) - count
            self.goods[name] = self.goods.get(name) + count
        else:
            self.goods[name] = count
            Store.goods[name] = Store.goods.get(name) - count

    @classmethod
    def input_count(cls, text):
        cls.text = text
        while True:
            try:
                cou = int(input(f'Введите количество оргтехники {text}: '))
                break
            except:
                print('Некорректный ввод, попробуйте снова!')
        return cou


class Depart(Store):
    goods = {}

    def transfer_to_store(self, name, count):
        if name in self.goods.keys():
            Store.goods[name] = Store.goods.get(name) + count
            self.goods[name] = self.goods.get(name) - count
        else:
            self.goods[name] = count
            Store.goods[name] = Store.goods.get(name) + count


print('Добавляем товар на слкад')
Store.add_goods('Printer', Store.input_count('Printer'))
Store.add_goods('Scaner', Store.input_count('Scaner'))
Store.add_goods('xerox', Store.input_count('xerox'))

Store.add_goods('Printer', Store.input_count('Printer'))
print('\nТовары на складе: ', Store.goods)

print('Переводим оргтехнику со склада в подразделение')
d = Depart()
d.transfer('Printer', d.input_count('Printer'))

print('\nТовары на складе после трансфера в подразделение: ', Store.goods)
print('\nТовары в подразделении: ', Depart.goods)

print('Переводим технику из подразделения на склад')
d.transfer_to_store('Printer', d.input_count('Printer'))

print('\nТовары на складе после трансфера из подразделения на склад: ', Store.goods)
print('\nТовары в подразделении: ', Depart.goods)
