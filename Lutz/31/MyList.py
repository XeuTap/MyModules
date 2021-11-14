import sys


class MyList(list):
    pass


class MyListSub(MyList):
    count = 0

    def __init__(self, __ls):
        self.count = self.count + 1
        self.extend(__ls)

    def __call__(self):
        print('вызов')


ls = MyList([1,2,3])

print(ls)

ls2 = ls + [1,2,3]

print(ls2)

ls3 = [1,2,3] + ls
print(ls3)


ls = MyListSub([4,5,6])
print(ls)
ls.append(1)

print(ls)

ls2 = ls + [1,2,3]

print(ls2)

ls3 = [1,2,3] + ls
print(ls3)

