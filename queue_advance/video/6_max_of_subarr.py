# Maximum in all subarrays of size k

# ex: [10, 8, 5, 12, 15, 7, 6], k=3. O/p: 10, 12, 15, 15, 15

# Naive solution: TC: O(n*k) SC: O(1)
# Consider every window of size k and find the maximum element in that window.

def printMax(arr,k):
    n = len(arr)
    for i in range(n-k+1):
        res = arr[i]

        for j in range(i+1,i+k):
            res = max(res, arr[j])
        print(res,end=" ")

arr = [10, 8, 5, 12, 15, 7, 6]
k = 3
printMax(arr,k)

# Efficient solution:
# Using deque
# Maintain a deque of size k and store max element in front of the deque.

from collections import deque

def printKMax(arr,k):
    n = len(arr)
    dq = deque()
    for i in range(k):
        while dq and arr[i]>=arr[dq[-1]] :
            dq.pop()
        dq.append(i)
    
    print(arr[dq[0]], end =" ")

    for i in range(k,n):
        while (dq and dq[0]<= i-k):
            dq.popleft()
        while (dq and arr[i]>=arr[dq[-1]]):
            dq.pop()
        dq.append(i)
        print(arr[dq[0]], end=" ")
    
arr = [10, 8, 5, 12, 15, 7, 6]
k = 3
print()
printKMax(arr,k)