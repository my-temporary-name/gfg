# Counting sort algorithm
# A O(n+k) time complexity sorting algorithm where n is the number of elements and k is the range of the input.
# Input in range 0 to k

# Naive approach: TC = O(n+k), SC = O(n+k)

def countingsort(arr,k):
    count = [0]*k
    for x in arr:
        count[x]+=1
    index = 0
    for i in range(k):
        for j in range(count[i]):
            arr[index]=i
            index+=1
    return arr

arr = [1,4,1,2,7,5,2]
k = 8
A = countingsort(arr,k)
print(A)


# the above approach is not in-place, we can make it in-place by using the same array for storing the count
# It will not work for an array of objects like an array of students to be sorted by their marks.

def CountSort(arr,k):
    output = [0]*len(arr)
    count = [0]*k

    for x in arr:
        count[x]+=1
    
    for i in range(1,k):
        count[i]+=count[i-1]
    
    for x in reversed(arr):
        output[count[x]-1] = x
        count[x]-=1

    for i in range(len(arr)):
        arr[i] = output[i]

arr = [1,4,1,2,7,5,2]
k = 8
CountSort(arr,k)
print(arr)

# this is not a comparison based sorting algorithm, 
# TC = OO(n+k), SC = O(n+k)
# It is stable algorithm, it maintains the relative order of equal elements.
