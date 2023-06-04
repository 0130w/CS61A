from isPrime import isPrime

def isPalindrome(n = 1):
    """ isPalindrome is a function that takes input
        as integer and returns True if it is a palindrome
        and False otherwise
        default param equals to 1
    
    >>> isPalindrome()
    True
    >>> isPalindrome(121)
    True
    >>> isPalindrome(125)
    False
    """
    string_n = str(n)
    length = len(string_n)
    for i in range(0, length//2):
        if string_n[i] != string_n[length - 1 - i]:
            return False
    return True

def isPalindromeAndPrime(n = 1):
    """ isPalindromeAndPrime is a function that takes input
        as integer and returns True if it's a palindrome and a prime
        at the same time and False otherwise
        default param equals to 1

    >>> isPalindromeAndPrime()
    True
    >>> isPalindromeAndPrime(121)
    False
    >>> isPalindromeAndPrime(1764671)
    True
    """
    if isPalindrome(n) and isPrime(n):
        return True
    return False

def palPrime(N = 1):
    """ palPrime is a function that takes input
        as integer and print k from 1..=N if
        k is both a palindrome and a prime
        default param equals to 1
    >>> palPrime()
    1
    >>> palPrime(5)
    1
    2
    3
    5
    """
    n = 1
    while n <= N:
        if isPalindromeAndPrime(n):
            print(n)
        n = n + 1


# A simpler way of writing isPalindrome is:
# return s == s[::-1]