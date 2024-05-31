# Allocate minimum number of pages
# Given an arr where each number represent the number of pages in a book and k number of students. 
# The books are arranged in the order of pages. We need to allocate the books to k students such that the maximum number of pages allocated to a student is minimum.

# Example: arr=[10,20,30,40], k=2; Output: 60
# Only contiguous allocation is allowed. So, the books will be allocated in the order of pages.

# Naive Approach: Time Complexity: O(n^k-1); 
# We need to choose k-1 cuts out of n-1 cuts. So, we will run a loop from 1 to n-k+1 and then for each cut, we will find the max of sum of pages of books.

def minPages(arr,n,k):
    if k==1:
        return sum(arr[0:n])
    if n==1:
        return arr[0]
    
    res = float("inf")

    for i in range(1,n):
        res = min(res, max(minPages(arr,i,k-1), sum(arr[i:])))
    
    return res

arr=[10,20,30,40]
k=2
n=len(arr)
print("Minimum number of pages allocated is: ",minPages(arr,n,k))


# Binary Search Approach: Here our input is not sorted
# Time Complexity: O(n log(sum of pages))

# Example: [10,20,10,30], k=2; Output: [30,40] answer will be in this range (maximum value, sum of all pages)

def isFeasible(arr,k,ans):  
    req,s = 1,0
    for i in range(n):
        if (s+arr[i])>ans:
            req+=1
            s=arr[i]
        else:
            s+=arr[i]
    return req<=k



def minPages(arr,k):
    n=len(arr)
    s= sum(arr)
    mx= max(arr)
    low,high= mx, s
    res = 0
    while low<=high:
        mid = (low+high)//2
        if (isFeasible(arr,k,mid)):
            res = mid
            high = mid-1
        else:
            low = mid+1
    return res

arr = [10,20,10,30]
k=2
print("Minimum number of pages allocated is: ",minPages(arr,k))