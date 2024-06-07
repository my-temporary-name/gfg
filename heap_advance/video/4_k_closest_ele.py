# K closest elements
# I/P = [10, 15, 7, 3, 4], k=2, x=8. O/P = [7,10]

# We have to find k elements such that they are closest to x.

# Naive approach: O(nk)

arr= [10, 15, 7, 3, 4]
k = 2
x = 8

for i in range(k):
    mi = 0
    for i in range(1,len(arr)):
        if abs(arr[mi]-x) > abs(arr[i]-x):
            mi = i
    print(arr[mi], end=" ") 
    arr.pop(mi)

# Efficient approach: 

import heapq
def kClosest(arr,x,k):
    n = len(arr)
    h = []
    for i in range(k):
        heapq.heappush(h,(-abs(arr[i]-x),i))
    
    for i in range(k,n):
        curr = -abs(arr[i]-x)
        p , pi = h[0]
        if curr>p:
            heapq.heappop(h)
            heapq.heappush(h,(curr,i))
    while h:
        p, pi = heapq.heappop(h)
        print(arr[pi], end=" ")

arr =[10, 31, 5, 40, 38, 80]
print()		
x = 35
k = 3
kClosest(arr,x,k)