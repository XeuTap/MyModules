from classtools import AttrDisplay


class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

#    def __str__(self):
#        return '[Person: {0}, {1}, {2}]'.format(self.job, self.name, self.pay)

    def lastName(self):  # Методы, реализующие поведение экземпляров
        return self.name.split()[-1]  # self – подразумеваемый экземпляр

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))  # Изменения придется вносить
        # только в одном месте


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=10):
        Person.giveRaise(self, percent + bonus)
        # self.pay = int(self.pay * (1 + percent + bonus))


if __name__ == '__main__':  # Только когда файл запускается для тестирования
    # реализация самотестирования
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)  # Экземпляр Manager: __init__
    tom.giveRaise(.10)  # Вызов адаптированной версии
    print(tom.lastName())  # Вызов унаследованного метода
    print(tom)  # Вызов унаследованного __str__
    print('--All three - -')
    for object in (bob, sue, tom):  # Обработка объектов обобщенным способом
        object.giveRaise(.10)  # Вызовет метод giveRaise этого объекта
        print(object)  # Вызовет общий метод __str__
    employes = {'bob': bob, 'sue': sue, 'tom': tom}
    print('Employes list')
    for obj in employes.values():
        print(obj)
