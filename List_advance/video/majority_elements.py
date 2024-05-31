# Find all the majority elements in an array
# Example 1: arr = [8,3,4,8,8] ; Output: [8]


# Naive Approach: Time complexity: O(n^2) ; Space complexity: O(1)

def Majority(arr,n):
    for i in range(n):
        count=1
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                count+=1
        if count>n/2:
            return arr[i]
    return -1 # If there is no majority element

arr = [8,3,4,8,8]
print("Using Naive Approach: ", Majority(arr,len(arr)))

# Efficient Approach: Time complexity: O(n) ; Space complexity: O(1)
# Moore's Voting Algorithm
# It is done in two steps:
# 1. Find a candidate for majority element
# 2. Check if the candidate is majority element

def Majority2(arr,n):
    res=0
    count=1
    for i in range(1,n):
        if arr[res]==arr[i]:
            count+=1
        else:
            count-=1
        if count==0:
            res = i
            count = 1

    count =0
    for i in range(0,n):
        if arr[res]==arr[i]:
            count+=1
    
    if count<=n//2:
        return -1
    return arr[res]

arr = [8,3,4,8,8]
print("Using Efficient Approach: ", Majority2(arr,len(arr))) # 8