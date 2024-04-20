import numpy as np
#create a random 3 by 4 matrix and a 4 by 1 vector
#The programmed random numbers are not actually random
from numpy.random import default_rng
rng=np.random.default_rng()

#The 3 by 4 matrix
#A=rng.random((3,4))
A=np.array([[1,2,3],[4,5,6]])
print(A)
#The vector
#x=rng.random((4,1))
x=np.array([[7],[8],[9]])
print(x)
#Multiply A by x
b=A@x
print(b)
#Write a program to matrix-vector multiplication
#using the psuedo-code we saw previously
n=2
m=3
b=np.zeros((n,1),dtype=int)
for i in range(n):
    for j in range(m):
        b[i]+=A[i][j]*x[j]
print(b)