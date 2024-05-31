# Longest common span with same sum in binary array
# We are given two binary arrays, we need to find the longest common span with same sum in both arrays.

# Example: arr1 = [0,1,0,0,0,0], arr2 = [1,0,1,0,0,1] : output = 4 i.e from index 0100 


# naive solution: TC=O(n^2)

def fLongCommonSpan(arr1,arr2):
    res = 0
    n = len(arr1)
    for i in range(n):
        sum1 = 0
        sum2 = 0

        for j in range(i,n):
            sum1+=arr1[j]
            sum2+=arr2[j]

            if sum1 ==sum2:
                res = max(res, j-i+1)
    return res

arr1 = [0,1,0,0,0,0]
arr2 = [1,0,1,0,0,1]
print(fLongCommonSpan(arr1,arr2))


# efficient solution: TC=O(n)
# 1. Compute the difference arr
# 2. Return length of the longest subarray with sum=0 in temp

def longCommonSpan(arr1,arr2):
    n = len(arr1)
    temp = [0]*n

    for i in range(n):
        temp[i] = arr1[i] - arr2[i]
        mydict = dict()

        sum = 0
        max_len = 0
        for i in range(n):
            sum+=temp[i]
            if sum==0:
                max_len = i+1
            if sum in mydict:
                max_len = max(max_len, i - mydict[sum])
            else:
                mydict[sum] = i
    return max_len

arr1 = [0,1,0,0,0,0]
arr2 = [1,0,1,0,0,1]
print(longCommonSpan(arr1,arr2))
