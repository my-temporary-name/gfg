# Sub array with sum 0
# Example: arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]; Output: Yes (3, 4, -7)
# Sub array is contiguous elements of an array.

# naive solution: tc = O(n^2)
# 1. Traverse through all subarrays
# 2. Calculate sum of each subarray
# 3. If sum is 0, return True
# if sum(arr[i:j]) == 0, return True

# Efficient solution:
# Idea is to use prefix sum and hashing both,


def isZeroSum(arr):
    pre_sum = 0
    h = set()

    for i in range(len(arr)):
        pre_sum+= arr[i]

        if pre_sum==0 or pre_sum in h:
            return True
        h.add(pre_sum)
    return False

arr = [3, 4, 7, 3, 1, 3, 1, -4, 2, 2]
print(isZeroSum(arr))