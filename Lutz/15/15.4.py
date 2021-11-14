L = [1, 2, 4, 8, 16, 32, 64]
pow2 = [2 ** x for x in range(0, 7)]
print(pow2)
X = 5
i = 0
find_to = 2 ** X    # ответ на e
while i < len(L):
    if 2 ** X == L[i]:
        break
    else:
        i = i+1
else:
    print('not found')

print('at index', i)

for i in L:
    if 2 ** X == i:
        print('at index', L.index(i))
        break
    else:
        i = 1+1
else:
    print('not found')

if 2 ** X in L:
    print('found at', L.index(2 ** X), 'index')
else:
    print('not found')