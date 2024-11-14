# st = {1, 2, 3, 4, 5}
# # sets can be used to perform most math operations as sets concept is also arrived from maths

A = {1, 3, 5}
B = {1, 2, 3, 4, 5}
print(A.issubset(B))
print(A.issuperset(B))

A = {1, 2, 3}
B = {3, 4, 5}
C1 = A.union(B)
C2 = A | B
print(C1, C2)

A = {1, 2, 3}
B = {3, 4, 5}
C1 = A.intersection(B)
C2 = A & B
print(C1, C2)

A = {1, 2, 3}
B = {3, 4, 5}
C1 = A.difference(B)
C2 = A - B
print(C1, C2)
