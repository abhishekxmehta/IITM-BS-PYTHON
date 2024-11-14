def initialize_mat(dim):
    C = []
    for i in range(dim):
        C.append([])
    for i in range(dim):
         for j in range(dim):
          C[i].append(0)
    return C

# print(initialize_mat(3))

def dot_product(u,v):
    dim = len(u)
    ans=0
    for i in range(dim):
        ans += u[i]*v[i]
    return ans

# x = [1,2,3]
# y = [7,1,2]
# print(dot_product(x,y))

def row(M,i):
    dim = len(M)
    l=[]
    for k in range(dim):
        l.append(M[i][k])
    return l

# A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# print(row(A,0))

def column(M,j):
    dim = len(M)
    l=[]
    for k in range(dim):
        l.append(M[k][j])
    return l

# A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# print(column(A,0))

def mat_mul(A, B):
    dim=len(A)
    C=initialize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j] = dot_product(row(A, i),column(B, j))
    return C

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [[1, 2, 1],[3, 1, 7],[6, 2, 4]]
C=mat_mul(A,B)
print(C)

import numpy

A = numpy.matrix(A)
B = numpy.matrix(B)
C=A*B
print(C)