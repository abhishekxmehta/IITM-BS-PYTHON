r1 = [1, 2, 3]
r2 = [4, 5, 6]
r3 = [7, 8, 9]

s1 = [1, 2, 1]
s2 = [6, 2, 3]
s3 = [4, 2, 1]

A = [r1, r2, r3]
B = [s1, s2, s3]

C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

dim = 3

# Manual matrix multiplication
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            C[i][j] += A[i][k] * B[k][j]

print("Manual multiplication result:")
print(C)

# Using numpy
import numpy

X = numpy.matrix(A)
Y = numpy.matrix(B)

print("Numpy multiplication result:")
print(X * Y)
