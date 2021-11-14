class Adder:
    def __init__(self, data):
        self.data = data

    def add(self, x, y):
        return 'Not Implemented'

    def __add__(self, other):
        return self.add(self.data, other)


class ListAdder(Adder):
    def add(self, x, y):
        return x + y


class DictAdder(Adder):
    def add(self, x, y):
        temp = { }
        for key, item in x.items():
            temp[key] = item
        for key, item in y.items():
            temp[key] = item
        return temp


test = Adder(0)
print(test.add(1, 2))
ls1 = [1, 2, 3]
ls2 = [11, 12, 13]
listTest = ListAdder([1, 2, 3])
print(listTest + ls2)
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'g': 5, 'h': 6, 'j': 7}
dictTest = DictAdder({'a': 1, 'b': 2, 'c': 3})
print(dictTest + dict2)
