# Purchase maximum items with given sum
# cost = [1, 12, 5, 111, 200], sum = 10. O/P = 2 (1,5)

# Find the maximum number of items that can be purchased with the given sum without exceeding the sum.


# Naive approach: TC = O(nlogn) 
cost = [1, 12, 5, 111, 200]
sum = 10

res = 0

cost.sort()

for i in cost:
    if i<=sum:
        sum-=i
        res+=1
    else:
        break

print(res) # 2

# Efficient approach: TC = O(n)

import heapq

def maxElement(cost,sum):
    res = 0
    pq = cost # min heap
    heapq.heapify(pq)

    for i in cost:
        top = heapq.heappop(pq)
        if top<=sum:
            sum-=top
            res+=1
        else:
            break
    return res

cost = [1, 12, 5, 111, 200]
sum = 10
print(maxElement(cost,sum)) # 2