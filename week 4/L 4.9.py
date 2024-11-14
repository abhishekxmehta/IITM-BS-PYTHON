# #let us write few functions on lists.
#
# def first_element(l):
#     return l[0]
#
# x = [1, 2, 3]
# print (first_element(x))
#
# def second_element(l):
#     return l[1]
#
# x = [1, 2, 3]
# print (first_element(x))
#

# # to find lowest number in list
# def list_min(l):
#     mini = l[0]
#     for i in range(len(l)):
#         if l[i] < mini:
#             mini = l[i]
#     return mini
#
# l = [7, 8, 9, 1, 40, -5, -100]
# print(list_min(l))
#
# #to find highest number in last
# def list_max(l):
#     maxi = l[0]
#     for i in range(len(l)):
#         if l[i] > maxi:
#             maxi = l[i]
#     return maxi
#
# l = [7, 8, 9, 1, 40, -5, -100]
# print(list_max(l))

# def list_appendbefore(l, z):
#     newl = []
#     for i in range(len(z)):
#         newl.append(z[i])
#     for i in range(len(l)):
#         newl.append(l[i])
#     return newl
#
# l = [7, 8, 9, 1, 40, -5, -100]
# z = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(list_appendbefore(l, z))

# def list_append(l, z):
#     newl = []
#     for i in range(len(l)):
#         newl.append(l[i])
#     for i in range(len(z)):
#         newl.append(z[i])
#     return newl
#
# l = [7, 8, 9, 1, 40, -5, -100]
# z = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(list_append(l, z))

# def list_average(l):
#     count = len(l)
#     total = 0
#     for i in l:
#         total += i
#     return total/count
#
# l = [7, 8, 9, 1, 40]
# print(list_average(l))

