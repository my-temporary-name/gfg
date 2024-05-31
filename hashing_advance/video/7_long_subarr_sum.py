# Find the length of longest subarray with given sum

# Naive solution to find all subarrays with given sum.


def lss(arr,sum):
    n = len(arr)
    res = 0
    for i in range(n):
        curr_sum=0
        for j in range(i,n):
            curr_sum+=arr[j]
            if curr_sum == sum:
                res = max(res, j-i+1)
    return res

arr = [5, 8, 6, 13, 3,10,1,9]
sum = 14

print(lss(arr,sum))

# Efficient solution:

def longestSubArray(arr,sum):
    n = len(arr)
    mydict = dict()
    pre_sum = 0
    res = 0
    for i in range(n):
        pre_sum+= arr[i]
        if pre_sum ==sum:
            res= i+1
        if pre_sum not in mydict:
            mydict[pre_sum]=i
        if pre_sum -  sum in mydict:
            res = max(res, i-mydict[pre_sum-sum])
    return res

arr = [5, 8, 6, 13, 3,10,1,9]
sum = 14
print(longestSubArray(arr,sum))