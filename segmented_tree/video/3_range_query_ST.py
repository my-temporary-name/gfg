# Range query  in Segmented Tree
# Write a function to get the sum of elements in the given range

arr =[10, 20, 30, 40]
n = len(arr)
tree = [0]*4*n

def buildTree(ss, se, si):
    if ss == se:
        tree[si] = arr[ss]
        return arr[ss]
    mid = (ss+se)//2
    tree[si] = buildTree(ss,mid, 2*si +1) + buildTree(mid+1, se, 2*si + 2)
    return tree[si]

def getSumReq(qs, qe, ss, se, si):
    if se<qs or ss>qe:
        return 0
    
    if qs<=ss and qe>=se:
        return tree[si]
    mid = (ss+se)//2
    return getSumReq(qs, qe, ss, mid, 2*si+1) + getSumReq(qs, qe, mid+1, se, 2*si+2)

buildTree(0,3,0)
print(getSumReq(0,2,0,n-1,0)) # 50