#  DEPTH FIRST SEARCH (DFS) ALGORITHM
#  DFS is a graph traversal algorithm that explores as far as possible along each branch before backtracking.

# EXAMPLE: 
#  0 ---- 1 ---- 4 ---- 5
#  |      |
#  2 ---- 3

# O/P: 0 -> 1 -> 3 -> 2 -> 4 -> 5
# 1. Start from the source vertex.
# 2. Visit the source vertex and mark it as visited.
# 3. Visit the adjacent vertex of the source vertex.
# 4. Repeat step 3 until there is no adjacent vertex.
# 5. Backtrack to the previous vertex and repeat step 3.


def DFS_Rec(adj,s,visited):
    visited[s] = True
    print(s, end = " ")

    for u in adj[s]: # For all adjacent vertices of s
        if visited[u] == False: # If u is not visited
            DFS_Rec(adj, u, visited) # Call DFS_Rec function with adjacency list, vertex u and visited list as input

def DFS(adj,s):
    visited = [False]*len(adj)
    DFS_Rec(adj, s, visited)

def printGraph(adj):
    for u, l in enumerate(adj):
        print(u, l)


adj = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 4], [1, 3]]

printGraph(adj)

DFS(adj, 0)

# In comparison to BFS, in DFS we use recursion to traverse the graph in depth. (DFS_Rec function is called recursively for each adjacent vertex of the source vertex.)

# DFS_Rec(0) -> DFS_Rec(1) -> DFS_Rec(3) -> DFS_Rec(2) -> DFS_Rec(4)
