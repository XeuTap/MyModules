s = 10
def mainfunc():
    print(s)
    def otherfunc():
        nonlocal b
        b = 20
    otherfunc()
    print(b)


mainfunc()
