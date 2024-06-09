# DFS for Disconnect Graph:
def DFS_Rec(adj,s,visited):
    visited[s] = True
    print(s, end = " ")

    for u in adj[s]: # For all adjacent vertices of s
        if visited[u] == False: # If u is not visited
            DFS_Rec(adj, u, visited) # Call DFS_Rec function with adjacency list, vertex u and visited list as input

def DFS(adj,s):
    visited = [False]*len(adj)
    # modified DFS to handle disconnected graph
    for u in range(len(adj)):
        if visited[u]==False:
            DFS_Rec(adj, u, visited)

def printGraph(adj):
    for u, l in enumerate(adj):
        print(u, l)


adj = [[1, 2], [0, 2], [0, 1], [4], [3]]

printGraph(adj)

DFS(adj, 0)