# Breadth First Search (BFS) algorithm
# Given an Undirected Graph and source vertex 's' , print BFS from given source vertex.

#   1--------3
#  /          \
# 0 -----------5
#  \          /
#   2--------4

# Output: 0   1 2 5   3 4 # Print yourself(0), print your friends (1,2,5), print your friends' friends (3,4)

from collections import deque

def BFS(adj, s): # Take adjacency list and source vertex as input

    visited = [False]*len(adj) # Create a list of False values of length equal to the number of vertices
    q = deque() # Create a queue
    q.append(s) # Add source vertex to the queue
    visited[s] = True # Mark source vertex as visited
    while q: # While queue is not empty
        s = q.popleft() # Pop the leftmost element from the queue and assign it to s
        print(s, end=" ") # Print the popped element
        for u in adj[s]: # For each vertex u in the adjacency list of s i.e. for each friend of s
            if visited[u] == False: # If u is not visited
                q.append(u) # Add u to the queue
                visited[u] = True # Mark u as visited

    # What happens in BFS function is that we start from the source vertex, print it, mark it as visited, add it to the queue.
    # Then we pop the leftmost element from the queue, print it, mark it as visited, add its friends to the queue.
    # We keep doing this until the queue is empty.

def printGraph(adj):
    for u, l in enumerate(adj):
        print(u,l)

v = 4

adj = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [2, 3]]

#   1-----------3
#  /|        / |
# 0 |     /    |
#  \|  /       |
#   2-----------4


printGraph(adj)
s = 0

print("BFS from source vertex 0:")
BFS(adj, s)
