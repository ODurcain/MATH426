import numpy as np

def lu_decomposition_banded(A, m_upper, m_lower):
    n = len(A)
    L = np.eye(n)
    U = np.copy(A)
    P = np.eye(n)

    # Decompose the banded matrix into lower and upper triangular matrices
    for i in range(n):
        if i < m_upper:
            start_col = 0
            end_col = min(n, i + m_lower + 1)
        elif i >= n - m_lower:
            start_col = max(0, i - m_upper)
            end_col = n
        else:
            start_col = max(0, i - m_upper)
            end_col = min(n, i + m_lower + 1)
            
        U[i, start_col:end_col] = A[i, start_col:end_col]
        
        if U[i, i] == 0:
            # If the pivot element is zero, perform row swapping
            for j in range(i+1, n):
                if U[j, i] != 0:
                    # Swap rows in U
                    U[[i, j]] = U[[j, i]]
                    # Swap rows in P
                    P[[i, j]] = P[[j, i]]
                    # Update the corresponding rows in L
                    L[[i, j], :i] = L[[j, i], :i]
                    break
            else:
                raise ValueError("Matrix is singular.")

        if i < n - 1:
            factor = U[i+1, i] / U[i, i]
            L[i+1, i] = factor
            U[i+1, start_col:end_col] -= factor * U[i, start_col:end_col]

    return P, L, U

    # for k in range(n-1):
    #     # Partial pivoting within the bandwidth
    #     max_row = k + np.argmax(np.abs(U[k:min(n, k+m_lower+1), k]))

    #     if max_row != k:
    #         U[[k, max_row]] = U[[max_row, k]]
    #         P[[k, max_row]] = P[[max_row, k]]
    #         if k > 0:
    #             L[[k, max_row], :k] = L[[max_row, k], :k]

    #     # Elimination within the bandwidth
    #     for i in range(k+1, min(n, k+m_upper+1)):
    #         factor = U[i, k] / U[k, k]
    #         L[i, k] = factor
    #         # Adjusted elimination step for the bandwidth
    #         start_col = max(0, k - m_lower)  # Start column index within bandwidth
    #         end_col = min(n, k + m_upper + 1)  # End column index within bandwidth
    #         U[i, start_col:end_col] -= factor * U[k, start_col:end_col]

    # return P, L, U

# Example usage with a banded matrix:
A_banded = np.array([[2, 1, -1, 0],
                      [-2, 0, 0, 0],
                      [0, 1, -2, 6],
                      [0, -1, 2, -3]], dtype=float)

m_upper = 1  # Upper bandwidth
m_lower = 1  # Lower bandwidth

P, L, U = lu_decomposition_banded(A_banded, m_upper, m_lower)
print("P:")
print(P)
print("L:")
print(L)
print("U:")
print(U)
