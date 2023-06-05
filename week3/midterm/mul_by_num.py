def mul_by_num(x):
    """ takes one argument and returns a one argument function that multiples any value passed to it by the original number
    
    >>> f = mul_by_num(5)
    >>> g = mul_by_num(2)
    >>> f(3)
    15
    >>> g(-4)
    -8
    """
    return lambda y: x*y