def alphabet_position(text):
    answ = ''
    for word in text:
        answ += str(char_to_int(word)) + ' '
    answ = answ.rstrip()
    return answ


def char_to_int(ch):
    alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if ch.isalpha():
        return alph.index(ch.upper()) + 1
    return ''

print(alphabet_position('asdkqwepk'))