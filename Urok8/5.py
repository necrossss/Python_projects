# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.


class Store:
    goods = {}

    # возможно классметод тут не особо и нужен...
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


class Depart(Store):
    goods = {}

    def transfer_to_store(self, name, count):
        if name in self.goods.keys():
            Store.goods[name] = Store.goods.get(name) + count
            self.goods[name] = self.goods.get(name) - count
        else:
            self.goods[name] = count
            Store.goods[name] = Store.goods.get(name) + count


Store.add_goods('Printer', 10)
Store.add_goods('Scaner', 20)
Store.add_goods('xerox', 5)

Store.add_goods('Printer', 20)
print('\nТовары на складе: ', Store.goods)

d = Depart()
d.transfer('Printer', 5)

print('\nТовары на складе после трансфера в подразделение: ', Store.goods)
print('\nТовары в подразделении: ', Depart.goods)

d.transfer_to_store('Printer', 5)

print('\nТовары на складе после трансфера из подразделения на склад: ', Store.goods)
print('\nТовары в подразделении: ', Depart.goods)
