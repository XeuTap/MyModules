def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars(counter=0, message='111')

def foo():
    foo.counter += 1
    print ("Counter is %d" % foo.counter)
    print(foo.message)
foo()
foo()
foo()

def myfunc():
  if not hasattr(myfunc, "counter"):
     myfunc.counter = 0  # it doesn't exist yet, so initialize it
  myfunc.counter += 1
  return myfunc.counter
print(myfunc())
print(myfunc())
print(myfunc())
print(myfunc())
print(myfunc())