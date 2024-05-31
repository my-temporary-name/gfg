# Find Peak Element in an Array
# Element is peak if it is greater than or equal to its neighbours
# There will be always at least one peak element in the array
# Example: [10,20,15,2,23,90,67], Output: 20 or 90

# Naive Solution: Time Complexity: O(n), Space Complexity: O(1)

def peak(arr):
    n = len(arr)
    if n==1:
        return arr[0]
    if arr[0]>=arr[1]: # First element is peak
        return arr[0]
    if arr[n-1]>=arr[n-2]: # Last element is peak
        return arr[n-1]
    
    for i in range(1,n-1):
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
            return arr[i]
    return -1

arr = [10,20,15,2,23,90,67]
print("Peak Element is: ",peak(arr))

# Efficient Solution: Time Complexity: O(log(n)), Space Complexity: O(1) ; Using Binary Search

def peak(arr):
    l=0
    h=len(arr)-1

    while l<=h:
        mid=(l+h)//2
        if ((mid==0 or arr[mid-1]<=arr[mid]) and (mid==len(arr)-1 or arr[mid+1]<=arr[mid])):
            return arr[mid]
        if mid> 0 and arr[mid]-1 >arr[mid]:
            h=mid-1
        else:
            l=mid+1
    return -1

arr = [10,20,15,2,23,90,67]
print("Using Efficient Solution: Peak Element is: ",peak(arr))