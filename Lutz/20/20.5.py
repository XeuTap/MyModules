def copyDict(dict):
    newDict = {}
    for key, val in dict.items():
        newDict[key] = val
    return newDict


def addDict(dict1, dict2):
    if type(dict1) == dict:
        answ = {}
        for key, val in dict1.items():
            answ[key] = val
        for key, val in dict2.items():
            answ[key] = val
    else:
        answ = [i for i in dict1] + [i for i in dict2]
    return answ

thisone= {'a': '1', 'b': '2'}
andthis = {'c': '3', 'd': '4'}

ls1 = [1,2,3]
ls2 = [4,5,6]

secondone = addDict(thisone, andthis)
newls = addDict(ls1, ls2)

print(secondone)
print(type(secondone))

ls1[0] = 0
ls2.pop(1)
print(newls)
print(type(newls))
