# Find Kth smallest element in an array

# example: arr=[10,5, 30, 12], k=2 : Output: 10

# Naive Solution: TC = O(nlogn) SC = O(1)
# sort the array and return kth element

def kth_smallest(arr,n,k):
    arr.sort()
    return arr[k-1]

arr = [10,5,30,12]
n = len(arr)
k = 2
print(kth_smallest(arr,n,k)) # 10

# Efficient Solution: TC = O(n) SC = O(1)
# Using Quick Sort Partitioning (in ideal case)



def partition(arr, l, r):
    x=arr[r]
    i = l
    for j in range(l,r):
        if arr[j]<=x:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
    arr[i],arr[r] = arr[r], arr[i]
    return i

def kth_small(arr,k):
    l = 0
    r = len(arr)-1

    while l<=r:
        p = partition(arr,l,r)
        if p == k-1:
            return arr[p]
        
        elif p>k-1:
            r = p-1
        
        else:
            l=p+1
    return -1

arr = [10,5,30,12]
k = 2
print(kth_small(arr,k)) # 10
