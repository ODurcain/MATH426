import numpy as np
from numpy.random import default_rng
# import random # option 2

# create a random 3x4 matrix, and a 4x1 vector
rng = np.random.default_rng()
# rand_num = random.randint(1, 100) # option 2

# matrix
# A =rng.random((3,4))
A = np.array(([1,2,3], [4,5,6]))
print(A)

# vector
# x=rng.random((4,1))
x = np.array(([7,8,9]))
print(x)

# multiply A by x
b=A@x
print(b)

# write a program to use matrix vector multiplication using the pseudocode from earlier
n=2
m=3
b=np.zeros((n,1), dtype=int)
for i in range (n):
    for j in range (m):
        b[i]+=A[i][j]*x[j]
print(b)

