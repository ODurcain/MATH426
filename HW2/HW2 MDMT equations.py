import numpy as np

def MDM_T_inner_product(A):
    n = len(A)
    iM = np.zeros((n, n))
    iD = np.zeros((n, n))

    for j in range(n):
        for i in range(j, n):
            sum_prod = sum(iM[i][k] * iM[j][k] * iD[k][k] for k in range(j))
            if i == j:
                iD[i][j] = A[i][j] - sum_prod
                iM[i][j] = np.sqrt(iD[i][j])
            else:
                iM[i][j] = (A[i][j] - sum_prod) / iD[j][j]

    return iM, iD

def MDM_T_outer_product(A):
    n = len(A)
    oM = np.zeros((n, n))
    oD = np.zeros((n, n))

    for j in range(n):
        for i in range(n):
            if i >= j:
                oM[i][j] = A[i][j] - sum(oM[i][k] * oD[k][k] * oM[j][k] for k in range(j))
            if i == j:
                oD[i][j] = A[i][i] - sum(oM[i][k] ** 2 * oD[k][k] for k in range(j))
                oM[i][j] = np.sqrt(oD[i][j]) 

    return oM, oD

def MDM_T_bordered(A):
    n = len(A)
    B = np.zeros((n + 1, n + 1))
    B[:-1, :-1] = A
    B[-1, :-1] = np.diag(A)

    L, U = LU_decomposition(B)

    M = L[:-1, :-1]
    D = np.diag(U[:-1, :-1])
    D_inv = np.diag(1 / D)

    return M, D, D_inv

def LU_decomposition(A):
    n = len(A)
    L = np.eye(n)
    U = np.copy(A)

    for i in range(n):
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j, i:] -= factor * U[i, i:]

    return L, U

# Example usage:
# A = np.array([[2,1,-1,3], 
#               [-2,0,0,0], 
#               [4,1,-2,6],
#               [-6,-1,2,-3]], dtype=int)

A=np.array([[4,0],
            [0,9]])

eigenvalues, _ = np.linalg.eig(A)
print("Eigenvalues of A:", eigenvalues)

iM, iD = MDM_T_inner_product(A)
print("iM:")
print(iM)
print("iD:")
print(iD)

oM, oD = MDM_T_outer_product(A)
print("oM:")
print(oM)
print("oD:")
print(oD)

M, D, D_inv = MDM_T_bordered(A)
print("M:")
print(M)
print("D:")
print(D)
print("D_inv:")
print(D_inv)
