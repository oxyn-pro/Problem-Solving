# TC: O(log n)
# SC: O(1)
def guessNumber(n, pick):
    """
    I changed the logic of the method a little and
    added the pick variable to be able to implement the guess method
    """
    l, r = 0, n

    while l <= r:
        middle = (l + r) // 2

        if guess(middle, pick) > 0:
            l = middle + 1
        elif guess(middle, pick) < 0:
            r = middle - 1
        else:
            return middle

    return -1


def guess(n, pick):
    if n > pick:
        return -1
    elif n < pick:
        return 1
    else:
        return 0


print(guessNumber(10, 6))
