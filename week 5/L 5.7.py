# #the x variable in the function is different from other x
# def myFunction1(x):
#     x = x * 2
#     print("Value of x in function 1",x)
#
# #the x variable in the function is different from other x
# def myFunction2(x):
#     x = x * 3
#     print("Value of x in function 2",x)
#
# #this x is a global variable and can be acessible throughout the program
# x = 5
# print("Value of x before function call",x)
#
# #we are just passing the value inside x we are not passing x
# myFunction1(x)
# #we are just passing the value inside x we are not passing x
# myFunction2(x)
#
#
# print("Value of x after function call",x)
#


#to use global variable x we could use



def myFunction1():
    global x
    x = x * 2
    print("Value of x in function 1:", x)

def myFunction2():
    global x
    x = x * 3
    print("Value of x in function 2:", x)

x = 5
print("Value of x before function call:", x)

myFunction1()
myFunction2()

print("Value of x after function call:", x)
