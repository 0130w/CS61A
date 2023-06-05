compose1 = lambda f,g: lambda x: f(g(x))

f = compose1

print(f(lambda x: x*x, lambda y: y+y)(2))

# Don't write code like this :(

lambda num: "even" if num % 2 == 0 else "odd"   # interesting