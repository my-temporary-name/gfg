# K largest elements
# I/P = [9,8,7,18,19,17], k=2. O/P = [18,19]

# max heap approach will take O(n+klogn) time complexity

# Instead of using max heap, we can use min heap.
# 1. Build a min heap with first k elements.
# 2. Traverse from (k+1)th element:
#   a. Compare current element with top of heap. if smaller than top, ignore it.
#   b. Else remove the top element and insert current element in the min heap.
# 3. Print contents of min heap.

import heapq as hq

def FirstKele(arr, size, k):
    minHeap =[]

    for i in range(k):
        minHeap.append(arr[i])
    hq.heapify(minHeap)

    for i in range(k,size):
        if minHeap[0] > arr[i]:
            continue
        else:
            minHeap[0] = minHeap[-1]
            minHeap.pop()
            minHeap.append(arr[i])
            hq.heapify(minHeap)

    for i in minHeap:
        print(i, end=" ")

arr = [9,8,7,18,19,17]
size = len(arr)
k = 2
FirstKele(arr, size, k)