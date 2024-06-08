# Merge K sorted Arrays

# Ex: [[1,3,5,7],[2,4,6,8],[0,9,10,11]]
# O/P: [0,1,2,3,4,5,6,7,8,9,10,11]

# Naive Approach: TC= O(nk log nk) , K = no of arrays, n = max no of elements in an array.
# 1. Pull all elements in a list.
# 2. Sort the list.

# Efficient Approach:
# Idea is to use min heap data structure.

# Recheck the code and understand the logic.

import heapq
def sortK(arr,k):
    n = len(arr)
    pq = arr[:k+1]
    heapq.heapify(pq)
    index = 0

    for i in range(k+1,n):
        arr[index] = heapq.heappop(pq)
        index+=1
        heapq.heappush(pq,arr[i])

        while pq:
            arr[index] = heapq.heappop(pq)
            index+=1

def printArr(arr):
    for i in arr:
        print(i, end=" ")

if __name__ == '__main__':
    k = 3
    arr = [2, 6, 12, 56, 8]
 
    sortK(arr, k)
 
    print("Sorted Array: ",end =" ")
 
    printArr(arr)