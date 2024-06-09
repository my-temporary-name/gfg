# DFS for Disconnect Graph: Tc = O(V+E)
def DFS_Rec(adj,s,visited):
    visited[s] = True
    print(s, end = " ")

    for u in adj[s]: # For all adjacent vertices of s
        if visited[u] == False: # If u is not visited
            DFS_Rec(adj, u, visited) # Call DFS_Rec function with adjacency list, vertex u and visited list as input

def DFS(adj,s):
    visited = [False]*len(adj)
    # modified DFS to handle disconnected graph
    res = 0 # to count number of connected components
    for u in range(len(adj)):
        if visited[u]==False:
            res+=1
            DFS_Rec(adj, u, visited)
    print("\nNumber of connected components:",res)

def printGraph(adj):
    for u, l in enumerate(adj):
        print(u, l)


adj = [[1, 2], [0, 2], [0, 1], [4], [3]]

printGraph(adj)

DFS(adj, 0)