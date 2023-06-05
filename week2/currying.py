def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h

print(curried_pow(2)(3))