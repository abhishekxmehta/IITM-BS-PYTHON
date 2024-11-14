#types of function arguments
def add(a, b, c):
    return (a + b - c)

print(add(20, 30, 40))


def add(c, a, b):
    return (a + b - c)

#this is known as keyword arguments where we defined everything
print(add(a = 20,b = 30,c = 40))



def add(c, a = 20, b = 30):
    return (a + b - c)

print(add(40))
print(add(40, 10))
print(add(40, 10, 50))

