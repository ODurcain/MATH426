import numpy as np

def ColeskINDecomp(MAT):
    n=MAT.shape[0]
    for i in range(n):
        for k in range(0,i-1):#Not executed when i=0
            MAT[i][i]-=MAT[k][i]**2
        if MAT[i][i]<=0:
            return'Matrix was not positive definite'
        else:
            MAT[i][i]=MAT[i][i]**0.5 #This is r_ii

        for j in range(i+1,n):#Do not execute if i=n
            for k in range(i-1):
                MAT[i][j]-=MAT[k][i]*MAT[k][j]
            MAT[i][j]=MAT[i][j]/MAT[i][i]#This is r_ij
    return MAT

A = np.array([[2,1,-1,3], 
              [-2,0,0,0], 
              [4,1,-2,6],
              [-6,-1,2,-3]])

MAT = ColeskINDecomp(A)
print(MAT)