data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = []
evens = [num for num in data if num % 2 == 0]
print(evens)

data = [1, 'one', 2, 'two', 3, 'three', 4, ' four']
words = []
words = [num for num in data if isinstance(num, str)]
print(words)

data = list('So long and thanks for all the fish;.split()')
title = []
title = [word.title() for word in data]
print(title)
