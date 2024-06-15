# Longest Increasing Subsequence (LIS) Problem
# In the Longest Increasing Subsequence (LIS) problem we are given an array and our goal is to find the longest increasing subsequence.
# Eg: arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
# Output: 6 (The longest increasing subsequence is 10, 22, 33, 50, 60, 80)

# Method 1: Recursion, Time Complexity: O(2^n) because at each step we have 2 choices
# Idea :
# Create a Lis array to store the length of LIS ending at each index


def LIS(arr):
    n = len(arr)
    lis = [1]*n # initialize LIS values for all indexes as 1 because each element is a subsequence of length 1

    for i in range(1,n):
        for j in range(0,i):
            if arr[i]>arr[j]:
                lis[i] = max(lis[i], lis[j]+1)
    res = lis[0]

    for i in range(n):
        res = max(lis[i], res)
    return res

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(LIS(arr)) # 6

# Method 2: Binary Search, Time Complexity: O(nlogn)
# Idea :
# We store the minimum possible tail value of the increasing subsequence of length i+1 in dp[i]

def ceilIndex(tail,x):
    l = 0
    r = len(tail)-1
    while r>l:
        m = l+(r-1)//2
        if (tail[m]>=x):
            r=m
        else:
            l = m+1
    return r

def LIS(arr):
    n = len(arr)
    tail = [arr[0]]

    for i in range(1,n):
        if arr[i]>tail[-1]:
            tail.append(arr[i])
        else:
            c = ceilIndex(tail,arr[i])
            tail[c] = arr[i]
    return len(tail)

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(LIS(arr)) # 6