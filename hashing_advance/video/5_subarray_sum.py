# Subarray with given sum
# arr = [5, 8, 6, 13, 3, -1]; sum = 22; Output: Yes (6, 13, 3)

# Naive solution: TC=O(n^2)
# Run two for  loops and check for every subarray sum.


# Efficient Solution:
# We will maintain variable size window.
# 1. While curr is smaller than sum, extend the window by increasing e
# 2. While curr is greater shrink the window by increasing s.


def isSubSum(arr,sum):
    s,curr=0,0
    for e in range(len(arr)):
        curr+=arr[e]
        while(curr>sum):
            curr-=arr[s]
            s+=1
        if curr == sum:
            return True
    return False

arr = [5, 8, 6, 13, -1, 3]
sum = 22
print(isSubSum(arr,sum))