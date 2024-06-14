# Union and Find operations in Disjoint Set Data Structure
# # Union: Join two subsets into a single subset.
# # Find: Determine which subset a particular element is in.

# eg: [0, 1, 2, 3, 4] , n=5
# 1. union(0,2) -> [0,2] [1] [3] [4]
# 2. union(2,4) -> [0,2,4] [1] [3]
# Now find operation will return 0,2,4 in the same subset
# 3. union(1,3) -> [0,2,4] [1,3]
# Now find operation will return 1,3 in the same subset

# To implement Union and Find operations, we can use Tree data structure, TC: O(n)

n = 5
parent = [i for i in range(n)]

def find(x):
    if parent[x]==x:
        return x
    return find(parent[x])

def union(x,y):
    x_rep = find(x)
    y_rep = find(y)
    if x_rep==y_rep:
        return
    parent[y_rep] = x_rep

union(0,2)
print(parent) # [0, 1, 0, 3, 4]
union(2,4)
print(parent) # [0, 1, 0, 3, 0]
union(1,3)
print(parent) # [0, 1, 0, 1, 0]
print(find(0)) # 0
print(find(1)) # 1
print(find(2)) # 0
print(find(3)) # 1
print(find(4)) # 0


# Time complexity:
# Worst case happens when the tree is skewed, TC: O(n)
