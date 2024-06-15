# Minimum Jump to reach end
# Given an array of non-negative integers, you are initially positioned at the first index of the array. 
# Each element in the array represents your maximum jump length at that position. 
# Your goal is to reach the last index in the minimum number of jumps.

# Eg: arr = [2,3,1,1,2,4,2,0,1,1] 
# Output: 4 (2->3->2->1->1)

# Eg: arr = [4,1,5,3,1,3,2,1,8]
# Output: 3 (4->5->3->8)

# Method 1: Recursion, Time Complexity: O(2^n) because at each step we have 2 choices

import sys

def minJumps(arr,n):
    if n==1:
        return 0
    res = sys.maxsize

    for i in range(n-1):
        if i+arr[i] >= n-1:
            sub_res = minJumps(arr, i+1)

            if sub_res!= sys.maxsize:
                res = min(res, sub_res+1)
    return res


arr = [2,3,1,1,2,4,2,0,1,1]
n = len(arr)
print(minJumps(arr,n)) # 4

# Method 2: Recursion + Memoization, Time Complexity: O(n^2)

import sys
def min_Jumps(arr):
    n = len(arr)
    dp=[sys.maxsize]*n
    dp[0]=0

    for i in range(1,n):
        for j in range(i):
            if (i<=j + arr[j]) and (dp[j!=sys.maxsize]):
                dp[i] = min(dp[i] , dp[j] +1)
                break
    return dp[n-1]

arr = [2,3,1,1,2,4,2,0,1,1]
print(min_Jumps(arr)) # 4