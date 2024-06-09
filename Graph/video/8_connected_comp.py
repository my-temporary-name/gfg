# Connected Components in an undirected graph using BFS, TC = O(V+E)

# Connected Components in an undirected graph  are the subgraphs in which all the vertices are connected to each other.

from collections import deque

def BFS(adj, s, visited):
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        s = q.popleft()
        for u in adj[s]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True



def BFSDis(adj):
    visited = [False] * len(adj)
    res = 0
    for u in range(len(adj)):
        if visited[u]==False: # If u is not visited
            res = res+1 # Increment the count of connected components
            BFS(adj, u, visited) # Call BFS function with adjacency list, vertex u and visited list as input
    return res # Return the count of connected components



def printGraph(adj):
    for u, l in enumerate(adj):
        print(u, l)


# main

v = 8

adj = [[1, 2], [0, 2], [0, 1], [4], [3], [6,7], [5],[5]]

printGraph(adj)

print('\nconnected component')
print('no of connected component',BFSDis(adj))
