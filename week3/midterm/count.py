def count(digit, num):
    """ Count how many times digit element appears in integer box
    >>> count(2, 222122)
    5
    >>> count(0, -2020)
    2
    >>> count(0, 0)
    0
    """
    if num == 0:
        return 0
    if num < 0:
        num = -num
    count = 0
    while(num != 0):
        value = num % 10
        if value == digit:
            count += 1
        num //= 10
    return count