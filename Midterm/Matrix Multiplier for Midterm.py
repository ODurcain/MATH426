# matrix multiplication

import numpy as np

A=np.array([[1,-2,-3],
            [0,1,2],
            [-1,-2,1]])
x=np.array([[-1],[2],[0]])
x_trans=np.transpose(x)
A_trans=np.transpose(A)
B=np.array([[-1,0,4],
            [-2,1,2],
            [0,-2,1]])
C=np.array([[-1,1,1],
            [-2,1,2],
            [1,-2,1]])
D=np.array([[-2,-1,4],
            [-2,1,1],
            [1,-2,1]])
B_trans=np.transpose(B)
C_trans=np.transpose(C)

#1
one_d=np.dot(np.dot(x_trans,A),x)

print("1d: ", one_d)

#2
two_a=np.dot(A,B)
two_b=np.dot(B,A)
two_c=A_trans
two_d=np.dot(B,A_trans)

print("2a: \n", two_a)
print("2b: \n", two_b)
print("2c: \n", two_c)
print("2d: \n", two_d)

#3
n1=np.block([[A,np.zeros_like(A)],[np.zeros_like(B),B]])
print("n1: \n", n1)
n2=np.block([[C,np.zeros_like(C)],[np.zeros_like(D),D]])
print("n2: \n", n2)