# Adjacency List implementation:

def addEdge(adj, u,v):
    adj[u].append(v)
    adj[v].append(u)

def printGraph(adj):
    for l in adj:
        print(l)

v=4
adj = [[] for i in range(v)] # We create a list of lists to represent the adjacency list
addEdge(adj, 0,1)
addEdge(adj, 0,2)
addEdge(adj, 1,2)
addEdge(adj, 1,3)

printGraph(adj)

# [1, 2]
# [0, 2, 3]
# [0, 1]
# [1]