import time
reps = 100000
repslist = range(reps)

def timer(func, *pargs, **kargs):
    """ Return time, function result"""
    start = time.time()
    for i in repslist:
        ret = func(*pargs, **kargs)
    result = time.time() - start
    return result, ret
