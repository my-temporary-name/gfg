# SLiding Window Technique

# Find the maximum sum of k consecutive elements in the array
# Example: [1,8,30,-5,20,7], k=3 ; Output: 

# Naive Approach: Time Complexity: O(n*k)

def maxKSum(arr, k):
    res = float("-inf")
    i =0
    n=len(arr)
    while(i+k-1<n):
        curr=0
        for j in range(k):
            curr+=arr[i+j]
        res = max(curr,res)
        i+=1
    return res

arr = [1,8,30,-5,20,7]
k = 3
print("Maximum sum of k consecutive elements in the array is: ",maxKSum(arr,k))

# Efficient Approach: Time Complexity: O(n) , It uses sliding window technique
# Here after every window slide, we will remove the first element and add the next element

def KMaxSum(arr,k):
    curr=0
    for i in range(k):
        curr+=arr[i]
    res=curr
    for i in range(k,len(arr)):
        curr=curr+arr[i]-arr[i-k]
        res=max(curr,res)
    return res

arr = [1,8,30,-5,20,7]
k = 3
print("Maximum sum of k consecutive elements in the array is: ",KMaxSum(arr,k))