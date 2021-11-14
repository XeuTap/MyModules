def countLines(name):
    return len(name.readlines())


def countChars(name):
    return len(name.read())


def test(name):
    with open(name, 'r') as file:
        print(countLines(file))
        file.seek(0)
        print(countChars(file))


if __name__ == '__main__':
    test('mymod.py')
