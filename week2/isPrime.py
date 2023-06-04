from math import sqrt

def isPrime(n = 7):
    """ isPrime is a function that takes as input
        an integer and returns True if it is prime
        and False otherwise
        default param equals to 7
    >>> isPrime()
    True
    >>> isPrime(9)
    False
    >>> isPrime(7)
    True
    >>> isPrime(797)
    True
    """
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 1
    return True