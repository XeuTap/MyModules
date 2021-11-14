class CustomError(Exception):
    pass


def oops():
    raise CustomError


def test_run():
    try:
        oops()
    except (IndexError, CustomError):
        print('Ошибка')

if __name__ == '__main__':
    pass