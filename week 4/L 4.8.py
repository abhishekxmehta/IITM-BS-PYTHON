# #introduction to functions
# def add (a, b):
#     ans = a + b
#     print(ans)
#
# add (1, 6)
# add(10, 72)
#
# def sub(a, b):
#     ans = a - b
#     print(ans)
#
# sub (10, 2)
# sub (70, 43)

# def discount(cost, d):
#     ans = cost-(cost*(d/100))
#     print(ans)

# discount(100, 7)
# discount(27447382, 13.7)

# add(17,5)+sub(100,3)+discount(1500, 7.5)

# def add(a, b):
#     ans = a + b
#     return ans
#
# a = 2
# b = 15
# ans = a + b + 10
# print (ans)

def discount(cost, d):
    ans = cost - (cost * (d / 100))
    return(ans)

print("Enter the cost price")
x = float(input())

print("Enter the discount rate")
y = float(input())

print(discount(x, y))