def binsearch(_arr, elem: int) -> int:
    """ Simple binary search """
    high = len(_arr) - 1
    low = 0
    while low <= high:
        mid = int((low + high) / 2)
        guess = _arr[mid]
        if guess == elem:
            return mid
        if guess > elem:
            high = mid -1
        elif guess < elem:
            low = mid + 1
    return None

