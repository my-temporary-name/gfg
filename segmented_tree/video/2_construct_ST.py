# Construct Segmented Tree , TC: O(n)
# I/P: [10,20,30,40]
# O/P: [100,30,70,10,20,30,40] 

# Idea for the construction of the segment tree:
# 1. Recursively build left subtree
# 2. Recursively build right subtree
# 3. fill the root node as sum of the left and right child

# arr = [10,20,30,40]
# n = len(arr)
# tree = [0]*(4*n)
# buildTree(0,3,0) # (segment start, segment end, index in tree array)


def buildTree(ss,se,si): # ss: segment start, se: segment end, si: index in tree array
    if ss == se:
        tree[si] = arr[ss]
        return arr[ss]
    mid = (ss+se)//2
    tree[si] = buildTree(ss,mid,2*si + 1) + buildTree(mid+1, se, 2*si + 2)
    return tree[si]

arr = [10,20,30,40]
n = len(arr)
tree = [0]*(4*n)
buildTree(0,n-1,0)
print(tree)