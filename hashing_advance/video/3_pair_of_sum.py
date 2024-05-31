# Given an array return a pair with the given sum
# Example: arr = [3, 8, 4, 7, 6, 1], sum = 14; Output: (6, 8) yes


# Naive approach:  TC= O(n^2), SC=O(1)

def prinsum(arr,x):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == x:
                return 1
    return 0

arr = [3, 8, 4, 7, 6, 1]
x=14
print(prinsum(arr,x))


# Efficient Approach: TC= O(n), SC=O(n)

def prinsum2(arr,x):
    us = set()
    for i in arr:
        if x-i in us:
            return 1
        us.add(i)
    return 0

arr = [3, 8, 4, 7, 6, 1]
x=14
print(prinsum2(arr,x))