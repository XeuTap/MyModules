def adder(**kargs):
    ls = list(kargs.values())
    summ = ls.pop(0)
    for arg in ls:
        summ += arg
    return summ

print(adder(one=1,two=2))
print(adder(first='1', second='2'))
print(adder(ls=[1, 2], ls2=[3, 4]))

