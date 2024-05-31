# subarray with given sum

# Example [3,2,0,4,7] , sum =6, Output: 1 to 3

# Naive Approach: Time Complexity: O(n^2)

def isSubSum(arr,sum):
    for i in range(len(arr)):
        curr=0
        for j in range(i,len(arr)):
            curr+=arr[j]
            if curr==sum:
                return True
    return False

arr = [3,2,0,4,7]
sum = 8
print(isSubSum(arr,sum))

# Effecient Approach: Time Complexity: O(n)
# Idea is to use sliding window technique
# 1. While curr is smaller than sum, keep adding elements to curr
# 2. while curr is greater than sum, remove elements from start

def isSubSum(arr,sum):
    s,curr=0,0
    for e in range(len(arr)):
        curr+=arr[e]
        while(curr>sum):
            curr-=arr[s]
            s+=1
        if curr==sum:
            return True
    return False

arr = [3,2,0,4,7]
sum = 6
print("Subarray with given sum is: ",isSubSum(arr,sum))