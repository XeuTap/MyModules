from person import Person, Manager # Импортирует наши классы
import shelve

bob = Person('Bob Smith') # Создание объектов для сохранения
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)
with shelve.open('persondb’') as db: # Имя файла хранилища
    for object in (bob, sue, tom): # В качестве ключа использовать атрибут name
        db[object.name] = object # Сохранить объект в хранилище