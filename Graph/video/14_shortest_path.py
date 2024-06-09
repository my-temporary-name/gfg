# Shortest path in unweighted graph, TC = O(V+E)

# We can find the shortest path in an unweighted graph using BFS.

from collections import deque

INT_MAX = 4294967295

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


def BFS(adj, s, dist):
    visited = [False]*len(adj)

    q = deque()
    visited[s] = True
    q.append(s)

    while q:
        u = q.popleft()
        for v in adj[u]:
            if visited[v] == False:
                dist[v] = dist[u]+1 # Shortest path from source to v is 1 more than shortest path from source to u
                visited[v] = True
                q.append(v)

if __name__ == "__main__":
    v = 4
    adj = [[] for i in range(v)]

    addEdge(adj, 0, 1)
    addEdge(adj, 1, 2)
    addEdge(adj, 2, 3)
    addEdge(adj, 0, 2)
    addEdge(adj, 1, 3)

    dist = [INT_MAX]*v
    dist[0] = 0
    BFS(adj, 0, dist)
    print(*dist)
