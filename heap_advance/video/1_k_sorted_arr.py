# K sorted array
# I/P = [9,8,7,18,19,17], k=2. O/P = [7,8,9,17,18,19]
# The target is to sort the array in ascending order such that each element is at most k distance away from its correct position.

# Approach:
# we wil use min heap

import heapq

def sortK(arr,k):
    n = len(arr)
    pq = arr[: k+1]
    heapq.heapify(pq)
    index = 0

    for i in range(k+1, n): # to push the element in the heap
        arr[index] = heapq.heappop(pq)
        index+=1
        heapq.heappush(pq,arr[i])
    
    while pq: # to pop the element from the heap
        arr[index] = heapq.heappop(pq)
        index+=1

def printArray(arr):
    for i in arr:
        print(i,end=" ")
        
k = 3
arr = [2,6,3,12,56,8]
sortK(arr,k)
print(arr)