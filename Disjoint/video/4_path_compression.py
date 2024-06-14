# Path Compression
# The idea is to make the path from the root to the node shorter by making every other node in the path point to its grandparent. 
# This way, the path length is reduced, and we can find the root in O(1) time.

n = 5 
parent = [i for i in range(n)]

def find(x) :
    if parent[x] == x :
        return x 
    parent[x] = find(parent[x]) # path compression, making every other node in the path point to its grandparent
    return parent[x]
    
    
print(find(3))

# time for m operations on n elements: O(m x alpha(n)), where alpha(n) is the inverse Ackermann function
# So the time complexity is nearly O(1) for m operations on n elements