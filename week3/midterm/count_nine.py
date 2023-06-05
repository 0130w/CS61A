def count_nine(digit, num):
    """ count_nine takes a digit and a non-negative integer and returns the number of times the digit appears in the integer
        and is not adjacent to a 9
    
    >>> count_nine(9, 99)
    0
    >>> count_nine(2, 222122)
    5
    >>> count_nine(1, 1911191)
    1
    >>> count_nine(9, 9)
    1
    """
    if num == 0:
        return 0
    flag = True # False if right side is 9
    count = 0
    while num != 0:
        if flag and (num // 10) % 10 != 9 and num % 10 == digit:
            count += 1
        if num % 10 == 9:
            flag = False
        else:
            flag = True
        num //= 10
    return count