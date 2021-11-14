S = input()
summ = 0
ls = []
dic = {}
for word in S:
    __ascii = ord(word)
    ls.append(__ascii)
    dic[word] = __ascii
    summ += __ascii
print(ls)
print(dic)
print(summ)

