# Minimum difference between any two elements in an array
# Example: arr = [1, 8, 12, 5, 18] : Output: 3 (|5-8|)

# if single element is present in array, return INF


# Naive solution: TC = O(n^2) SC = O(1)
# Traverse through all pairs and find the minimum difference

def minDiff(arr):
    res = float("inf")
    for i in range(1,len(arr)):
        for j in range(i):
            res = min(res, abs(arr[i]-arr[j]))
    return res

arr = [1, 8, 12, 5, 18]
print(minDiff(arr)) # 3


# Efficient solution: TC = O(nlogn) SC = O(1)
# 1. sort the array
# 2. Traverse through the array and find the minimum difference between adjacent elements
# 3. return the minimum difference

def findMinDiff(arr):
    res = float("inf")
    arr.sort()

    for i in range(1, len(arr)):
        res = min(res, abs(arr[i] - arr[i-1]))
    return res

arr = [1, 8, 12, 5, 18]
print(findMinDiff(arr)) # 3