# l1 = [1,2,3]
# l2 = [10,20,30]
# l12 = l1 + l2
# l21 = l2 + l1
# print(l12,l21)

# l1 = [0,0,0,0,0,0,0,0,0,0]
# print(l1)

# #we can simplify this code using

# l1 = [0] * 10
# print(l1)

# l1 = [0] * 10
# print(l1)
# l2 = [1,2,3] * 5
# print(l2)

# # *LOGICAL OPERATORS*

# l1 = [1,2,3]
# l2 = [1,2,3]
# l3 = [1,3,2]
# print(l1 == l2)
# print(l2 == l3)
# print(l2 < l3)

# print([1,2] < [2,1])
# print([1] < [1,2,3])
# print([2,3] < [3])
# print([] < [1])

# # *MUTABILITY*

# l = [1,2,4]
# print(l)
# # we can update list in specific location in python
# # lists are mutable in python
# l[2] = 3
# print(l)

# #now lets try mutability with a string
#
# l=[1,2,4]
# print(l)
# l[2] = 3
# print(l)
#
# s='abce'
# print(s[3])
# s[3]='d'
# print(s)
# #it shows an error
# # we can access specific index in string but we cannot modify it in python

# x = 5
# y = x
# x = 10
# print(x,y)
# #this will print 10 5 as we expect it to print
#
# l1 = [1,2,3]
# l2 = l1
# l1[0] = 100
# print(l1,l2)
# #here we expect it to print [100 ,2 ,3] [1 ,2 ,3] but it prints [100, 2, 3] [100, 2, 3]
# # because in lists when we say l2 to the value of l1 it doesnt create new memory of l2 it just copies from l1 while it created new memory in the above code
#
# #if we want to create new memory location for l2 lets see how to do that below

# l1 = [1,2,3]
# #these are the three options below to create new memory
# l2 = list(l1)
# l3 = l1[:]
# l4 = l1.copy()
#
# l2[0] = 100
# l3[1] = 200
# l4[2] = 300
#
# print(l1,l2,l3,l4)

# # now one may ask how to verify that the list is using same or different memmory location or not
# # to veirfy this we could use is operator given below
#
# l1 = [1,2,3]
# l2 = list(l1)
# l3 = l1[:]
# l4 = l1.copy()
# l5 = l1
#
# #if it says true than there is simply two names given to same memory location
# print(l1 is l2)
# print(l1 is l3)
# print(l1 is l4)
# print(l1 is l5)


# def add(x):
#     x += 1
#     return x
#
# x = 5
# print(add(x))
# print(x)

# def add(x):
#     x.append(1)
#     return x
#
# x = [5]
# print(add(x))
# print(x)
#
#
#                     l = [1,2,3]
#                     print(l)
#
#                     l.append(4)
#                     print(l)
#
#                     l.remove(2)
#                     print(l)
#
#                     x = l.copy()
#                     print(x,l)
#
#                     l.insert(2,9)
#                     print(l)
#
#                     l.remove(2)
#                     print(l)
#
#                     l.pop(0)
#                     print(l)

#sort
# l = [2,6,1,50,3,7,5]
# l.sort()
# l.reverse()
# print(l)