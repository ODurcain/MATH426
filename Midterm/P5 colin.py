import numpy as np

def my_norm(matrix, type=None, p=2):
    n = matrix[0].size
    highest_sum = 0

    if type == "inf":
        for i in range(n):
            col_sum = 0
            for j in range(n):
                col_sum = col_sum + abs(matrix[i][j])
            highest_sum = max(col_sum, highest_sum)
    elif type == "1":
        for j in range(n):
            row_sum = 0
            for i in range(n):
                row_sum = row_sum + abs(matrix[i][j])
            highest_sum = max(row_sum, highest_sum)
    else: 
        for i in range(n):
            for j in range(n):
                highest_sum = highest_sum + (abs(matrix[i][j]) ** p)
        highest_sum = highest_sum ** (1/p)
    return highest_sum

def condition_number(matrix, type=None, p=2):
    return my_norm(matrix,type=type,p=p) * my_norm(np.linalg.inv(matrix),type=type,p=p)


mat = np.array([[1000,999],[999,998]])
mat2 = np.array([[3,2,9],[1,4,6],[8,5,2]])

print("My 2-Condition Number of matrix 1: " + str(condition_number(mat,p=2)))
print("Numpy's 2-Condition Number of matrix 1: " + str(np.linalg.cond(mat,2)))

print("My 2-Condition Number of matrix 2: " + str(condition_number(mat2,p=2)))
print("Numpy's 2-Condition Number of matrix 2: " + str(np.linalg.cond(mat2,2)))