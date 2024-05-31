# Find maximum sum subarray in a circular array
# Example: [5,-2,3,4] => 12 i.e 3+4+5

# Naive Approach: Time complexity: O(n^2), Space Complexity = O(1)


def maxCircularSum(l,n):
    res = l[0]
    for i in range(0,n):
        curr_max = l[i]
        curr_sum = l[i]

        for j in range(1,n):
            index = (i+j)%n
            curr_sum+= l[index]
            curr_max = max(curr_max, curr_sum)
        res = max(res, curr_max)
    return res

l = [5,-2,3,4]
n = len(l)

print("Using 2 for loops: ",maxCircularSum(l,n))


# Efficient Approach: Time complexity: O(n), Space Complexity = O(1)
# Idea:
# 1. Maximum sum of normal subarray. (Easy: Use Kadane's algorithm)
# 2. Maximum Sum of subarray that wraps around. (Difficult) 

def normalMaxSum(arr, n):
    res =arr[0]
    maxEnding = arr[0]
    for i in range(1,n):
        maxEnding = max(maxEnding + arr[i], arr[i])
        res = max(res, maxEnding)
    return res

def overallMaxSum(arr, n):
    max_normal = normalMaxSum(arr, n)
    if max_normal < 0: # In case all elements are negative
        return max_normal
    
    arr_sum =0
    for i in range(0,n):
        arr_sum+=arr[i]
        arr[i]= -arr[i] # Do the inversion of array elements
    max_circular = arr_sum + normalMaxSum(arr,n) # Now find the maximum sum of inverted array
    
    return max( max_circular, max_normal)

n=4
arr=[5, -2, 3, 4]
print("Using 1 for loop: ",overallMaxSum(arr, n))