# matrix multiplication

import numpy as np

x_trans=np.array([[-1,2,0]])
A=np.array([[1,-2,-3],[0,1,2],[-1,-2,1]])
x=np.array([[-1],[2],[0]])

B=np.array([[-1,0,4],[-2,1,2],[0,-2,1]])

h1=([[1,0,2],[0,1,3],[0,0,0]])
h2=([0,4,2])

one_d=np.dot(np.dot(x_trans,A),x)

two_a=np.dot(A,B)

two_b=np.dot(B,A)

hed=np.dot(h1, h2)

print("1d: ", one_d)

print("2a: \n", two_a)

print("2b: \n", two_b)

print("Hedral: \n", hed)