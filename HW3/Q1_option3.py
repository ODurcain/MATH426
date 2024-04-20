import numpy as np

def lu_decomposition(A, m_upper, m_lower): # m values added for banded matricies
    n = len(A) # square matrix, so can use len. If A wasn't a square it would be weird
    L = np.eye(n) # .eye() is handy and makes identity matricies of size n
    U = np.copy(A) #.astype(float)  # Make U float type. This was causing an error
    P = np.eye(n)

    for k in range(n-1):
#######################################################################################################
        # Partial pivoting: Find the row with maximum absolute value in the current column
        # max_row = np.argmax(np.abs(U[k:, k])) + k
        max_row = k + np.argmax(np.abs(U[k:min(n, k+m_lower+1), k])) # updated for banded matricies

        # Swap rows in U and P matrices
        if max_row != k:
            U[[k, max_row]] = U[[max_row, k]]
            P[[k, max_row]] = P[[max_row, k]]
            if k > 0:
                L[[k, max_row], :k] = L[[max_row, k], :k]

## This section can be removed, or commmented out and it is a traditioinal LU decomposition
#######################################################################################################

        # Elimination
        # for i in range(k+1, n):
        #     factor = U[i, k] / U[k, k]
        #     L[i, k] = factor
        #     U[i, k:] -= factor * U[k, k:] # error was here 
                
        # Elimination within the bandwidth
        for i in range(k+1, min(n, k+m_upper+1)):
            factor = U[i, k] / U[k, k]
            L[i, k] = factor
            U[i, k:min(n, k+m_upper+1)] -= factor * U[k, k:min(n, k+m_upper+1)]

    return P, L, U

# Example usage:
A = np.array([[2, 1, -1, 3],
              [-2, 0, 0, 0],
              [4, 1, -2, 6],
              [-6, -1, 2, -3]], dtype=float) # make og matrix float then no error arises

m_upper = 1  # Upper bandwidth
m_lower = 1  # Lower bandwidth

P, L, U = lu_decomposition(A, m_upper, m_lower)
print("P:")
print(P)
print("L:")
print(L)
print("U:")
print(U)


