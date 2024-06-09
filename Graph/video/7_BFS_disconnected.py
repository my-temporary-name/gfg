# BFS of Disconnected Graph, TC = O(V+E)

# Disconnected Graph is a graph in which there is no path between some pairs of vertices.
# Also, in a disconnected graph, there may be some vertices that are unreachable from all other vertices.
# Example: [[1, 2], [0, 3], [0, 3], [1, 2], [5, 6], [4, 6], [4, 5]]

from collections import deque

def BFS(adj,s,visited): # Take adjacency list, source vertex and visited list as input
    q= deque() # Create a queue
    q.append(s)# Add source vertex to the queue
    visited[s] = True # Mark source vertex as visited

    while q: # While queue is not empty
        s = q.popleft() # Pop the leftmost element from the queue and assign it to s
        print(s, end=" ") 
        
        for u in adj[s]: # For each vertex u in the adjacency list of s
            if visited[u] == False: # If u is not visited
                q.append(u) # Add u to the queue
                visited[u]=True # Mark u as visited

def BFSDisconnected(adj):
    visited = [False]*len(adj) # Create a list of False values of length equal to the number of vertices

    for u in range(len(adj)): # For each vertex u in the adjacency list
        if visited[u]==False: # If u is not visited
            BFS(adj, u, visited) # Call BFS function with adjacency list, vertex u and visited list as input

def printGraph(adj):
    for u, l in enumerate(adj):
        print(u, l)

v =7 # Number of vertices

adj =[[1, 2], [0, 3], [0, 3], [1, 2], [5, 6], [4, 6], [4, 5]]

printGraph(adj) 

print("BFS from source vertex 0:")
BFSDisconnected(adj)

# What we are doing in above code is that we are calling BFS function for each vertex in the adjacency list.
# This way, we are able to print BFS of all the vertices in the graph.
