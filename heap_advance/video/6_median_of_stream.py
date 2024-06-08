# Median of Stream
# Given an array of numbers, find the median of the numbers in the stream at every point.

# EX: [20,10,30,7] , O/P = [20,15,20,15]
# Naive Approach: TC= O(n^2)
# 1. Maintain sorted array.
# 2. For every element, insert it in the sorted array.
# 3. Find the median.

# Better Approach: TC= O(n log n)
# Augmented Binary Search Tree.
# 1. Maintain two heaps. One max heap and one min heap.
# 2. Insert the elements in the max heap.
# 3. If the size of max heap is greater than min heap, then pop the top element from max heap and push it to min heap.
# 4. If the size of min heap is greater than max heap, then pop the top element from min heap and push it to max heap.
# 5. If the size of both heaps are equal, then the median is the average of top elements of both heaps.
# 6. If the size of max heap is greater than min heap, then the top element of max heap is the median.
# 7. If the size of min heap is greater than max heap, then the top element of min heap is the median.
# 8. O/P the median.
# 9. Repeat the process for all elements in the array.
# 10. TC= O(n log n)

# More Efficient Approach: TC= O(n log n)
# 1. We will maintain 2 containers. 
# 2. One container will contain smaller half of the elements and other container will contain larger half of the elements.


import heapq

arrmax = []
arrmin = []
median = 0.0
 
class Solution:
    arrmax = []
    arrmin = []
    median = 0.0
 
    def balanceHeaps(self):
        
        if abs (len(arrmax) - len(arrmin))  > 1: 
 
            if len(arrmax) > len(arrmin):
                heapq.heappush(arrmin, -heapq.heappop(arrmax))
                
            else:
                heapq.heappush(arrmax, -heapq.heappop(arrmin))
        
 
                
    def getMedian(self):
        if (len(arrmax) + len(arrmin)) % 2 == 0:
            median = (-arrmax[0] + arrmin[0]) / 2
 
        else: 
            if len(arrmin) == 0:
                median = -arrmax[0]
                
            elif len(arrmin) < len(arrmax):
                median = -arrmax[0]
 
            else:
                median = arrmin[0]
 
        return median
        
    def insertHeaps(self,x):
 
        if len(arrmax) == 0:
            heapq.heappush(arrmax, -x)
 
        elif x > -arrmax[0]:
            heapq.heappush(arrmin, x)
 
        elif len(arrmin) == 0:
            heapq.heappush(arrmin, -heapq.heappop(arrmax))
            heapq.heappush(arrmax, -x)
 
        else :
            heapq.heappush(arrmax, -x)
 
 
        self.balanceHeaps()

arr = [20,10,30,7]
ob = Solution()
for i in arr:
    ob.insertHeaps(i)
    print(ob.getMedian(), end=" ")
print()
