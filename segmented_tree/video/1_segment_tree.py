# Segment Tree
# It is a data structure that allows answering range queries over an array effectively, while also being flexible enough to allow modifying the array. 
# This includes finding the sum of consecutive array elements a[l…r], or finding the minimum element in a such a range in O(logn) time. 
# Between answering such queries the Segment Tree allows modifying the array by replacing one element, or even change the elements of a 
# whole subsegment (e.g. assigning all elements a[l…r] to any value, or adding a value to all element in the subsegment).

# 1. Leaf represents the elements of the array
# 2. Each internal node represents some merging of the leaf nodes. The merging operation is a function of the elements it represents.
# 3. The root node represents the whole array

# Get sum of elements in given range

# Method 1: Simple Approach, TC: O(n)

def getsum(qs,qe):
    sum=0
    for i in range(qs,qe+1):
        sum += arr[i]
    print(sum)

def update(i, new_val):
    global arr
    arr[i] = new_val

arr = [1, 3, 5, 7, 9, 11]
getsum(1,3) # 15
update(2,10)
getsum(1,3) # 20
print()
# Method 2: Segment Tree, TC: O(n)
# 1. Create prefix sum array to get the sum of elements in the given range

def getSum(qs,qe):
    return ps[qe] if qs==0 else ps[qe] - ps[qs-1]

def update(i, new_val):
    global ps
    diff = new_val - arr[i]
    for j in range(i,n):
        ps[j] += diff

def initialize():
    global ps
    ps[0] = arr[0]
    for i in range(1,n):
        ps[i] = ps[i-1] + arr[i]


arr = [1, 3, 5, 7, 9, 11]
n = len(arr)
ps = [0]*n

initialize()
print(getSum(1,3)) # 15
update(2,10)
print(getSum(1,3)) # 20


# Motivation for using Segment Tree:
# segment tree for [10,20,30,40,50,60]
#                              210 [0,5]
#                             /      \
#                         60 [0,2] 150 [3,5]
#                         /     \       /    \
#                     30 [0,1] 30 [2,2] 90 [3,4] 60 [5,5]
#                     /    \          /    \       
#                 10 [0,0] 20 [1,1] 40 [3,3] 50 [4,4]  
# [210,60,150,30,30,90,60,10,20,x,x,40,50,x,x] x is dummy node
# left child = 2*i+1
# right child = 2*i+2
# parent = (i-1)//2
# if n is no. of elements in input array, then size of segment tree = 2*(2**ceil(log2(n)))-1 < 4*n
