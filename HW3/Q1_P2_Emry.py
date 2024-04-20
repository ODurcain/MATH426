import numpy as np

# for this algorithm we assume there are no zeros on the main diagonal, only works in this case.
# p and q are how many diagonals exist above and below the main diagonal
def get_diagonals(A, p , q):
 n = len(A)
 
 number_of_diagonals = p + q + 1

 #creates a multidimensional array with (p + q + 1) lists of length n to store each band and their elements
 banded_storage = [[] for j in range(number_of_diagonals)] 

 for i in range (n): # iterate through the rows
  for j in range(max(0, i - p), min(n, i + q + 1)): # making sure we are in range of the matrix

   # gets the position relative to the main diagonal, if (i-j) < 0 we are dealing with the bands ABOVE the main diagonal. If (i-j) > 0, we are dealing with bands BELOW the main diagonal.
   row = p + (i - j) 

   banded_storage[row].append(A[i][j])
 
 return banded_storage

def gaussian_elim(A, p, banded_storage):
 n = len(A)
 L = np.eye(n)
 U = np.zeros((n,n))

 # add the 1st entry of the main diagonal to U
 U[0,0] = banded_storage[p][0]

 # perform Thomas Algorithm
 for i in range(1, n):
  row = p + i - (i - 1)
  L[i, i-1] = banded_storage[row][i - 1] / U[i - 1, i - 1]
  U[i, i] = banded_storage[p][i] - L[i, i-1]*banded_storage[0][i-1]
 

 print(L)
 print()
 print(U)


A = np.array([
    [2, 3, 0, 0],
    [1, 4, 5, 0],
    [0, 2, 7, 8],
    [0, 0, 3, 9]
])

p = 1  
q = 1  

compact_storage = get_diagonals(A, p, q)
print(compact_storage)

gaussian_elim(A, p, compact_storage)