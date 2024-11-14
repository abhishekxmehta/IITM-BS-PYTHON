# below is an example of packing and unpacking
t = 1, 2, 3
print(t, type(t))


#unpacking
x, y, z = t
print(x, y, z)

x = 5
y = 10
x,y = y,x
print(x,y)

l = [10]
print(l, type(l))

#whenever we create a tuple which is () and just one element inside it python consider it as a single value instead of a tupple
t = (10)
print(t, type(t))

#to create a tuplle with just one element use ,
t = (10,)
print(t, type(t))

t = ([1, 2], ['a', 'b'])
print(t)

# #tuplles are immutable we cannot change its value
# t = ([1, 2], ['a', 'b'])
# t[0] = [10, 20]
# print(t)

#we  cannot modify tupple value but WE CAN MODIFY LISTS VALUE inside a tupple
t = ([1, 2], ['a', 'b'])
t[0][0] = [10, 20]
print(t)

# *
#if tupple is immutable then it is considered hashable
#if tupple is mutable then it is considered non-hashbale
# *