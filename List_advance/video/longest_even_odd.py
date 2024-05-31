# Find longest subarray with even and odd elements
# Example: [10,12,14,7,8] => 3 i.e [14,7,8]

# Naive Approach: Time complexity: O(n^2)

# l = [5, 10, 20, 6, 3, 8]
# n = len(l)
# res =1

# for i in range(0,n):
#     curr =1
#     for j in range(i+1, n):
#         if ((l[j]%2==0 and l[j-1]%2!=0) or (l[j]%2!=0 or l[j-1]%2==0)) :
#             curr+=1
#         else:
#             break
#     res =max(curr, res)

# print("Using 2 for loops: ",res)

def maxEvenOdd(arr, n):
    res=1 
    for i in range(0, n):
        curr=1 
        for j in range(i+1, n):
            if((arr[j]%2==0 and arr[j-1]%2!=0) or  (arr[j]%2!=0 and arr[j-1]%2==0)):
                curr+=1 
            else:
                break
        res=max(res, curr)
    return res
    
n=6
arr=[5, 10, 20, 6, 3, 8]
print(maxEvenOdd(arr, n))

# Efficient Approach: Time complexity: O(n)

def maxEvenOdd(arr, n):
    res=1 
    curr =1
    for i in range(1,n):
        if (arr[i]%2==0 and arr[i-1]%2!=0) or (arr[i]%2!=0 and arr[i-1]%2==0):
            curr+=1 
            res = max(res, curr)
        else:
            curr=1
    return res
    
    
n=6
arr=[5, 10, 20, 6, 3, 8]
print(maxEvenOdd(arr, n))