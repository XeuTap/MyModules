def isuniqe(_str):
    letters_list = []
    for letter in _str:
        if letter in letters_list:
            return 'Deja Vu'
        letters_list.append(letter)
    return 'Unique'


inputdata = 'aaaaaghhjjkl'
uniqedata = 'abcdef'

print(isuniqe(inputdata))
print(isuniqe(uniqedata))