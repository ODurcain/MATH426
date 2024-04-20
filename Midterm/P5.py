import numpy as np

def my_norm(matrix, p=2):
    n = matrix.shape[0]  # Get the number of rows in the matrix
    highest_sum = 0

    if p == np.inf:
        for j in range(n):
            col_sum = 0
            for i in range(n):
                col_sum += abs(matrix[i][j])
            highest_sum = max(col_sum, highest_sum)
    elif p == 1:
        for i in range(n):
            row_sum = 0
            for j in range(n):
                row_sum += abs(matrix[i][j])
            highest_sum = max(row_sum, highest_sum)
    else: 
        for i in range(n):
            for j in range(n):
                highest_sum += abs(matrix[i][j]) ** p
        highest_sum = highest_sum ** (1/p)
    return highest_sum

def condition_number(matrix, p=2):
    return my_norm(matrix, p=p) * my_norm(np.linalg.inv(matrix), p=p)

mat = np.array([[1000,999],[999,998]])
mat2 = np.array([[3,2,9],[1,4,6],[8,5,2]])

print("My 2-Condition Number of matrix 1: " + str(condition_number(mat, p=2)))
print("Numpy's 2-Condition Number of matrix 1: " + str(np.linalg.cond(mat, 2)))

print("My 2-Condition Number of matrix 2: " + str(condition_number(mat2, p=2)))
print("Numpy's 2-Condition Number of matrix 2: " + str(np.linalg.cond(mat2, 2)))
