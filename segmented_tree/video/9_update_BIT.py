# Binary Indexed Tree (Update)

arr = [10,20,30,40,50,60,70,80,90]
BITTree = [0]*(len(arr)+1)

def addbit(BITTree, n, i, v):
    i+=1
    while i<=n:
        BITTree[i] += v
        i += i & (-i)

def construct(arr, n):
    for i in range(n):
        addbit(BITTree, n, i, arr[i])

def updateBit(i,x):
    i+=1
    while i<=len(BITTree):
        BITTree[i] += x
        i += i & (-i) 

construct(arr,len(arr))
print(BITTree)
updateBit(2,10)
print(BITTree)
