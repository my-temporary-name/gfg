# Search in an Infinite Sorted Array

# Example: [1,10,15,20,40,80,90,100,200,500,1000,2000,5000,10000,20000,50000], x=100; Output: 7

# Naive Solution: Time Complexity: O(position), Space Complexity: O(1)

def search(arr,x):
    i=0
    while True:
        if arr[i]==x:
            return i
        if arr[i]>x:
            return -1
        i+=1

arr = [1,10,15,20,40,80,90,100,200,500,1000,2000,5000,10000,20000,50000]
x = 1001
print("Element found at position: ",search(arr,x))

# Efficient Solution: Time Complexity: O(log(position)), Space Complexity: O(1)
# Here we will use binary search technique

def binary_search(arr,l,r,x):

	if r >= l:
		mid = l+(r-l)//2

		if arr[mid] == x:
			return mid

		if arr[mid] > x:
			return binary_search(arr,l,mid-1,x)

		return binary_search(arr,mid+1,r,x)

	return -1
    

def search(arr,x):
    if arr[0]==x:
        return 0
    i=1
    while arr[i]<x:
        i=i*2
    
    if arr[i]==x:
        return i
    
    return binary_search(arr, i//2+1, i-1,x)

arr = [1,10,15,20,40,80,90,100,200,500,1000,2000,5000,10000,20000,50000]
x = 100

print("Using Efficient Solution: Element found at position: ",search(arr,x))