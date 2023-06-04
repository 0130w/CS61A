def return_two_things(x, y):
    return(x+y, x*y)
    print(x,y)  # unreachable

(s, p) = return_two_things(2, 5)
