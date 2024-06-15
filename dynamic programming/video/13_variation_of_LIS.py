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

# 4. Building Bridges TC: O(nlogn)
# You are given a pair of cities and the time taken to travel between them. You need to find the maximum number of bridges that can be built such that no two bridges cross each other.
# Eg: [[6,2],[4,3],[2,6],[1,5]]-> 2 (build bridges between [1,5] and [2,6])
# Idea:
# a. sort the array in increasing order of first element of pair. If 2 pairs have same first element then sort them in decreasing order of second element.
# b. find the LIS of the second element of the pairs.

# 5. Longest Chain of Pairs
# You are given n pairs of numbers. In each pair, the first number is smaller and the second number is larger. 
# You need to find the longest chain of pairs such that each pair is a[i][0]<a[i+1][0] and a[i][1]<a[i+1][1]
# EG: [[5,24],[39,60],[15,28],[27,40],[50,90]]-> 3 (chain is [5,24]->[27,40]->[50,90]) 
# Idea:
# a. sort the array in increasing order of first element of pair.
# b. find the LIS of the second element of the pairs.
