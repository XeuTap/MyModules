import timer

names = ['dwaynekaiser', 'rythm 2', 'rick_sanchez_2', 'frog', 'кот', 'rythm',
         'msx', 'pisyastic', 'skillezs1337', 'nekolover', 'test-bot', 'sadanton', 'sharfik', 'sawok99',
         'молчите бляди я принцесса', 'мастхэв', 'joshuabess', 'jojoojojhb', 'jlexa', 'haters21', 'шаверма',
         '123213123123', 'valerusik', 'noname1782[sns]', 'trash-bot', 'harlequin', 'ａｈｅｇａｏ', 'ajesetave', 'кексик💞',
         'marijavartanova', 'patchbot', 'ыфвsad', 'nmaer', 'liquote',
         'your father(mobile)',
         'dead inside in trap',
         'whitepride']
print(names)
names.sort()
print(names)
elem = 'мастхэв'
dicnames = { 'dwaynekaiser': 521428651284365313,
             'rythm 2': 252128902418268161,
             'rick_sanchez_2': 675781058666561603,
             'frog': 378940723656916992,
             'кот': 221241565492936704,
             'rythm': 235088799074484224,
             'msx': 269035415703388160,
             'pisyastic': 329593330533138442,
             'skillezs1337': 318853372591472662,
             'nekolover': 353645928957083648,
             'test-bot': 710783210174414858,
             'sadanton': 343434851787079691,
             'sharfik': 410782693786386434,
             'sawok99': 387270946542714884,
             'молчите бляди я принцесса': 201023230360682497,
             'мастхэв': 311168787040829450,
             'joshuabess': 571989052962635786,
             'jojoojojhb': 571990930824101908,
             'jlexa': 231798652396503040,
             'haters21': 439387557122408458,
             'шаверма': 222019488843825152,
             '123213123123': 408637768198127616,
             'valerusik': 519193912439603216,
             'noname1782[sns]': 393395046264602625,
             'trash-bot': 672508852549189660,
             'harlequin': 96978571817394176,
             'ａｈｅｇａｏ': 116567879263977473,
             'ajesetave': 284245391342436353,
             'кексик💞': 267639844090544128,
             'marijavartanova': 279551715332587521,
             'patchbot': 402528814548254720,
             'ыфвsad': 596821650780192779,
             'nmaer': 306794030497529856,
             'liquote': 261603912077934592,
             'your father(mobile)': 221260018878644224,
             'dead inside in trap': 320857560074944512,
             'whitepride': 221214499594698752 }

# ls_names = list(dicnames.keys())
# ls_names.sort()

def binsearch(names, elem, ls_names=None):
    if type(names) == dict:
        if ls_names is None:
            ls_names = list(dicnames.keys())
            ls_names.sort()
        high = len(ls_names) - 1
        low = 0
        while low <= high:
            mid = int((low + high) / 2)
            guess = ls_names[mid]
            if guess == elem:
                return names[ls_names[mid]]
            if guess > elem:
                high = mid - 1
            elif guess < elem:
                low = mid + 1
    else:
        high = len(names) - 1
        low = 0
        while low <= high:
            mid = int((low + high) / 2)
            guess = names[mid]
            if guess == elem:
                return mid
            if guess > elem:
                high = mid - 1
            elif guess < elem:
                low = mid + 1


def find_member(dic, name):
    if name in dic:
        return int(dic[name])
    return None


def find_member_broote(dic, name):
    for key, value in dic.items():
        if key == name:
            return value
    return None


print(timer.timer(binsearch, names, elem), 'Binary search through a list')
print(timer.timer(find_member, dicnames, elem), 'Search in the hash-table')
print(timer.timer(binsearch, dicnames, elem), 'Binary search for a dict')
print(timer.timer(find_member_broote, dicnames, elem), 'Broote force search')
