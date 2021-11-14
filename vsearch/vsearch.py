def search4vowels(phrase: str) -> set :
    """ Function finds an vowels in the str """
    vowels = set('aeoiu', )
    return vowels.intersection((set(phrase)))


def search4letters(phrase: str, letters: str = 'aeiou') -> set :
    """ Function finds a set of letters in the phrase"""
    return set(letters).intersection((set(phrase)))
