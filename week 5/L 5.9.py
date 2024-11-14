fruits = ['mango', 'apple', 'orange', 'pineapple', 'watermelon', 'banana', 'guava', 'kiwi']

bascket = iter(fruits)

print(next(bascket))

print(next(bascket))

print(next(bascket))

# for fruit in fruits:
#     print(fruit)


def square(limit):
    x = 0
    while x < limit:
        yield x * x
        yield x * x * x
        x += 1


a = square(5)
print(next(a), next(a), next(a), next(a))
print(next(a), next(a), next(a), next(a))
print(next(a), next(a))

