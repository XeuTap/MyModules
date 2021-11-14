import math
import time
reps = 1000000
repslist = range(reps)
def timer(func, *pargs, **kargs):
    start = time.time()
    for i in repslist:
        ret = func(*pargs, **kargs)
    result = time.time() - start
    return result, ret


ls = [2, 4, 9, 16, 25]


def forMethod():
    newls = []
    for n in ls:
        newls.append(math.sqrt(n))
    return newls


def mapMethod():
    newls = list(map(math.sqrt, ls))
    return newls


def genMethod():
    newls = [math.sqrt(i) for i in ls]
    return newls


print(timer(forMethod))
print(timer(mapMethod))
print(timer(genMethod))