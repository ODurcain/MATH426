import numpy as np

def lu_decomposition(A, m):
    n = len(A) # len only works for a square matrix
    L = np.eye(n) # Makes identity matrix of size n
    U = np.zeros((n, n)) # Sets upper matrix to 0's of size nxn

    for k in range(n-1):
        # For pivoting
        ##################################################################
        max_row = max(range(k, min(k+m+1, n)), key=lambda i: abs(A[i][k]))
        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]  # swap rows for partial pivoting
            L[[k, max_row], :k] = L[[max_row, k], :k]  # update L for row swapping
        ##################################################################

        for i in range(k+1, min(k+m+1, n)):
            factor = A[i][k] / A[k][k]
            L[i][k] = factor
            for j in range(k, min(k+m+1, n)):
                A[i][j] -= factor * A[k][j]

    # Upper Matrix handling
    for i in range(n):
        U[i][i:] = A[i][i:]

    return L, U

# Test:
A = np.array([[2, 3, 0, 0],
              [1, 4, 5, 0],
              [0, 2, 7, 8],
              [0, 0, 3, 9]], dtype=float)

m = 1  # bandwidth
L, U = lu_decomposition(A, m)
print("L:")
print(L)
print("U:")
print(U)
