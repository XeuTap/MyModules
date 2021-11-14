def isPrime(y):
    x = y // 2   # Для значений y > 1
    while x > 1:
        if y % x == 0:   # Остаток
            print(y, 'has factor', x)
            break   # Обойти блок else
        x = x-1
    else:   # Обычный выход
        print(y, 'is prime')


isPrime(13)
isPrime(13.0)
isPrime(15)
isPrime(15.0)