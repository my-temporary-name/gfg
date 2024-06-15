# Variation of Longest Increasing Subsequence (LIS) Problem

# 1. Minimum Deletions to make a sequence sorted
# eg: [5,10,3,6,7,8]-> [5,10] to get [3,6,7,8] so 2 deletions are required so output is 2

# 2. Maximum Sum Increasing Subsequence
# eg: [1,101,2,3,100,4,5]-> [1,2,3,100] so output is 106 

def maxSIS(arr):
    msis=[x for x in arr]
    for i in range(1, len(arr)):
        for j in range(i):
            if(arr[j]<arr[i]):
                msis[i]=max(msis[i], arr[i]+msis[j])
    return max(msis)

arr = [1,101,2,3,100,4,5]
print(maxSIS(arr)) # 106

# 3. Longest Bitonic Subsequence (LBS)
# A sequence is called Bitonic if it is first increasing and then decreasing.
# eg: [1,11,2,10,4,5,2,1]-> [1,2,10,4,2,1] so output is 6
# a. build LIS array from left to right, lis = [1,2,2,3,3,4,2,1]
# b. build LDS array from right to left, lds = [1,5,2,4,3,3,2,1]
# c. find max(lis[i]+lds[i]-1) for i in range(n)