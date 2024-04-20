# HW1 Q2

import numpy as np

# The matricies

# n x m, m=rows, n=columns
A=np.array([[1,-2,2,0],
            [-3,-1,4,-2]])
print("\nMatrix A:")
print(A)

# n x p, n=rows, p=columns
X=np.array([[2,0,-1],
            [3,-2,1],
            [0,2,-1],
            [3,-1,2]])
print("\nMatrix X:")
print(X)

# Attaining the 
m_A, n_A=A.shape
n_X, p_X=X.shape

# check if the matrices can be multiplied
if n_A == n_X:
    print("\nA rows, or m:")
    print(m_A)
    print("\nA columns, or n:")
    print(n_A)
    print("\nX rows, or n:")
    print(n_X)
    print("\nX columns, or p:")
    print(p_X)
elif n_A != n_X:
    raise ValueError("Can't do that champ")

# Multiply A by X
B = np.matmul(A, X)
# B = A @ X
print("\nMatrix B:")
print(B)

# Create empty matrix
C=np.zeros((m_A, p_X), dtype=int)

# Perform matrix multiplication
for i in range(m_A):
    for j in range(p_X):
        for k in range(n_A):  
            C[i][j] += A[i][k] * X[k][j]
print("\nMatrix C:")
print(C)

if np.array_equal(B, C):
    print("\nMatrix B and Cp match\n")
else:
    print("\nThey don't match\n")