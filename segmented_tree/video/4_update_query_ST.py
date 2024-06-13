# Update Query on segment tree:

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

def update_query(ss, se, i, si, diff):
    if i<ss or i>se:
        return
    tree[si] += diff
    if se>ss:
        mid = (ss + se)//2
        update_query(ss, mid, i, 2*si+1, diff)
        update_query(mid+1, se, i, 2*si+2, diff)



buildTree(0,3,0)
update_query(0,3,1,0,5)
print(tree) # [65, 25, 30, 40]