# Maximum sum with no consecutive elements
# Given an array of positive numbers, find the maximum sum of a subsequence with the constraint that no 2 numbers in the sequence 
# should be adjacent in the array. 

# eg: [1,10,2] -> 10 
# eg: [8,7,6,10] -> 18 (8+10)

# Naive approach: TC: O(2^n) using recursion
# we have two choice for each element, either include it or exclude it
# we first consider choice for last item
# a. maxREC(arr, n-2) + arr[n-1] (include the last element)
# b. maxREC(arr, n-1) (exclude the last element)

def maxSum(arr):
    n = len(arr)
    dp = [None]* (n+1)

    dp[1] = arr[0]
    dp[2] = max(arr[0], arr[1])

    for i in range(3,n+1):
        dp[i] = max(dp[i-1], # exclude the current element
                    dp[i-2]+arr[i-1]) # include the current element
    return dp[n]

arr = [8,7,6,10]
print(maxSum(arr)) # 18

# Method 2: Recursion + Memoization, TC: O(n)

def maxSum(arr):
    prev_prev = arr[0]
    prev = max(arr[0],arr[1])
    res = prev
    
    for i in range(3,len(arr)+1):
        res = max(prev,prev_prev + arr[i-1]) # include the current element or exclude it
        prev_prev = prev 
        prev = res
        
    return res
    
    
    
arr = [8,7,6,10]

print(maxSum(arr))