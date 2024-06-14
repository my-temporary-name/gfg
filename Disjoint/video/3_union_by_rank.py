# Union by rank:
# 1. We use an extra array rank[] in union operation.
# 2. It  typically stores the height of the tree rooted at i.
# 3. the idea is to make representative of the smaller height tree point to the representative of the larger height tree.

n = 5
parent = [i for i in range(n)]
rank = [0 for i in range(n)]
def find(x):
    if parent[x]==x:
        return x
    return find(parent[x])

def union(x,y):
    x_rep = find(x)
    y_rep = find(y)

    if x_rep == y_rep:
        return
    
    if rank[x_rep]<rank[y_rep]:
        parent[x_rep]=y_rep
    
    elif rank[x_rep]>rank[y_rep]:
        parent[y_rep]=x_rep
    
    else:
        parent[y_rep] = x_rep
        rank[x_rep] += 1
    return (parent,rank)

union(0,2)
print(parent) # [0, 1, 0, 3, 4]
union(2,4)
print(parent) # [0, 1, 0, 3, 0]
union(1,3)
print(parent) # [0, 1, 0, 1, 0]


# Now time complexity: O(logn)