# Search in a Sorted Rotated Array
# Example: [10,20,40,60,5,8], x=5; Output: 4

# Naive Solution: Time Complexity: O(n), Space Complexity: O(1)

arr = [10,20,40,60,5,8]
x = 5

for i in arr:
    if x==i:
        print("Element found at position: ",arr.index(i))
        break


# Efficient Solution: Time Complexity: O(log(n)), Space Complexity: O(1)
# One half of the array will always be sorted. Take middle element and compare it with the end element on both sides to find which half is sorted

def search(arr,l,r,x):

    # Like normal binary search
    l=0
    h=len(arr)-1
    while l<=h:
        mid= (l+h)//2
        if arr[mid]==x:
            return mid
        
        # Left half is sorted
        if arr[l]<arr[mid]:
            if arr[l]<=x<arr[mid]:
                h=mid-1
            else:
                l=mid+1
        
        # Right half is Sorted
        else:
            if arr[mid]<x<=arr[h]:
                l=mid+1
            else:
                h=mid-1
    return -1

arr = [10,20,40,60,5,8]
x = 5
print("Using Efficient Solution: Element found at position: ",search(arr,0,len(arr)-1,x))