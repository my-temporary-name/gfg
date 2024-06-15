# 0/1 Knapsack Problem
# The 0/1 Knapsack problem is a variation of the knapsack problem where we are given a set of items, 
# each with a weight and a value, and we need to determine the number of each item to include in a collection 
# so that the total weight is less than or equal to a given limit and the total value is as large as possible.
# We can either include an item or exclude it, we cannot include a fraction of an item.

# Example
# values = [10, 40, 30, 50] ,weights = [5, 4, 6, 3], W = 10
# Output: 90 (40+50) for weights [4,3]


def knapSack(w,wt,val,n): # w is the maximum weight, wt is the weight array, val is the value array, n is the number of items
    if n==0 or w==0:
        return 0
    if wt[n-1]>w: # if the weight of the nth item is greater than the maximum weight then we cannot include it
        return knapSack(w,wt,val,n-1)
    else:
        return max(val[n-1]+knapSack(w-wt[n-1],wt,val,n-1),knapSack(w,wt,val,n-1)) # if we include the nth item or exclude it
    
values = [10, 40, 30, 50]
weights = [5, 4, 6, 3]
W = 10
n = len(values)
print(knapSack(W,weights,values,n)) # 90

# Time Complexity: O(2^n) because at each step we have 2 choices

# Method 2: Recursion + Memoization, Time Complexity: O(n*w) where n is the number of items and w is the maximum weight

def knapSack2(w,wt,val,n):
    n = len(wt)
    dp = [[0 for x in range(w+1)] for x in range(n+1)] # create a 2D array to store the results of subproblems

    for i in range(1,n+1):
        for j in range(1,w+1):
            if wt[i-1] <= j:
                dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][w]

values = [10, 40, 30, 50]
weights = [5, 4, 6, 3]
W = 10
n = len(values)
print(knapSack2(W,weights,values,n)) # 90