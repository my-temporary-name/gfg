# Matrix chain multiplication
# Given a sequence of matrices, find the most efficient way to multiply these matrices together.
# Given an array p[] which represents the chain of matrices such that the ith matrix Ai is of dimension p[i-1] x p[i].
# eg: arr[2,1,3,4]
# Matrix1: 2x1 , Matrix2: 1x3, Matrix3: 3x4

# Idea : mChain(arr,i,k) +  mChain(arr,k,j)+arr[i]*arr[j]*arr[k] where i<k<j
# the above equation states that we are multiplying the matrices from i to k and k to j and then multiplying the result of these two matrices

def mChain(arr,i,j):
    if(i+1==j):
        return 0
    
    res = float('inf')
    for k in range(i+1,j):
        res = min(res,
                  mChain(arr,i,k) +  mChain(arr,k,j)+arr[i]*arr[j]*arr[k]
                  )
    
    return res
    
arr = [2,1,3,4]

print(mChain(arr,0,len(arr)-1))

# Dynamic Programming approach: TC: O(n^3)
# We have to get result cell that is dp[0][n-1]

def mChain(arr):
    n = len(arr)
    dp = [[None for i in range(n)] for x in range(n)]
    
    for i in range(0,n-1):
        dp[i][i+1]=0
        
    for gap in range(2,n):
        for i in range(0,n-gap):
            j = i+gap 
            dp[i][j] = float('inf')
            for k in range (i+1,j):
                dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j] + arr[i]*arr[k]*arr[j])
    
    return dp[0][n-1]
        
    
arr = [2,1,3,4]

print(mChain(arr))