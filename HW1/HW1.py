# Owen Durkin
# HW1 1/25/24
import numpy as np

# matricies

A=np.array([[1,3,2],
            [2,1,1],
            [-1,0,1]])
print("\nMatrix A=\n", A, "\n")

X=np.array([[1,0,1],
            [2,1,1],
            [-1,2,0]])
print("\nMatrix X=\n", X, "\n")

B=np.array([[5,7,4],
            [3,3,3],
            [-2,2,-1]])
print("\nMatrix B=\n", B, "\n")

# partitioning matricies

A_blocks = [
    [A[:2, :1], A[:2, 1:]],
    [A[2:, :1], A[2:, 1:]]
]

print("\nBlock Partitioning for matrix A:")
print("New A11\n", A_blocks[0][0])
print("New A12\n", A_blocks[0][1])
print("New A21\n", A_blocks[1][0])
print("New A22\n", A_blocks[1][1])

X_blocks = [
    [X[:1, :1], X[:1, 1:]],
    [X[1:, :1], X[1:, 1:]]
]

print("\nBlock Partitioning for matrix X:")
print("New X11\n", X_blocks[0][0])
print("New X12\n", X_blocks[0][1])
print("New X21\n", X_blocks[1][0])
print("New X22\n", X_blocks[1][1])

B_blocks = [
    [B[:2, :1], B[:2, 1:]],
    [B[2:, :1], B[2:, 1:]]
]

print("\nBlock partitioning for matrix B:")
print("New B11\n", B_blocks[0][0])
print("New B12\n", B_blocks[0][1])
print("New B21\n", B_blocks[1][0])
print("New B22\n", B_blocks[1][1])

# matrix multiplication

# proof for AX=B
print("\n")
b=A.dot(X)
print(b)
print(B)
if np.array_equal(B, b):
    print("They match\n")
else:
    print("They don't match\n")

# proof for a11x12+a12x22=b12

# n, m = A.shape 
n=3
m=3
b = np.zeros((n, m), dtype=int)

for i in range(n):
    for j in range(m):
        b[i] += A[i][j] * X[i][j]

print("Resultant Matrix b:")
print(b)