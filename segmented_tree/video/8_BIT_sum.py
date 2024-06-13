# Binary Indexed Tree (Prefix Sum)

# to get sum of first i elements in arr
# i = i+1
# Result = bitTree[i] + biTree[parent(i)] + bitTree[parent(parent(i))] + ....till we reach child of root(0) node


arr = [10,20,30,40,50,60,70,80,90]
BITree = [0]*(len(arr)+1)

def addbit(BITree, n, i, v):
    i+=1
    while i<=n:
        BITree[i] += v
        i += i & (-i)

def construct(arr, n):
    for i in range(n):
        addbit(BITree, n, i, arr[i])

def getSum(i):
    i = i+1
    res = 0
    while i>0:
        res = res+BITree[i]
        i = i -(i&(-i)) # this will give parent of i
    return res

construct(arr, len(arr))
print(BITree)
print(getSum(6))