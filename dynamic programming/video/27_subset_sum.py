# Subset sum problem
# Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
# Eg; [10, 5, 2, 3, 6], sum=8
# O/p: 2 # 5+3 , 2+6

# Recursive approach: TC: O(2^n)
def countSubsetSum(arr,n,sum):
    if n==0:
        if sum==0:
            return 1 
        else:
            return 0
        
    return countSubsetSum(arr,n-1,sum) + countSubsetSum(arr,n-1,sum-arr[n-1]) # either include the current element or exclude it
        
arr = [1,2,3,5,6,7]
n=6
sum = 8 

print(countSubsetSum(arr,n,sum))

# Dynamic Programming approach: TC: O(n*sum)


def CountSubsets(arr,sum):
    n = len(arr)
    dp = [[0 for i in range(sum+1)] for j in range(n+1)] # mat[i][j] will store the number of subsets of arr[0:i] with sum equal to j

    for i in range(n+1):
        dp[i][0] = 1 # if sum=0, then there is always one subset, the empty subset
    
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if j<arr[i-1]: # if the current element is greater than the sum, then we can't include it
                dp[i][j] = dp[i-1][j] # exclude the current element
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]] # either include the current element or exclude it
    return dp[n][sum] # return the number of subsets with sum equal to given sum
 
arr = [1,2,3,5,6,7]
sum = 8
print(CountSubsets(arr,sum))