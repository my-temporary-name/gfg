# Dijkstra's Shortest Path Algorithm,O((V + E) log V) for adjacency list.
# Dijkstra's algorithm is very similar to Prim's algorithm for minimum spanning tree. 
# Like Prim's MST, we generate a SPT (shortest path tree) with given source as root. 
# We maintain two sets, one set contains vertices included in shortest path tree, other set includes vertices not yet included in shortest path tree. 
# At every step of the algorithm, we find a vertex which is in the other set (set of not yet included) and has a minimum distance from the source.

# Only difference is that we use a priority queue to store the vertices instead of key[] array.

# It doesn't work for negative weight edges, Bellman-Ford works for negative weight edges.
# Does the shortest path change if add a weight to all the edges? Yes, it changes.

# Implementation:
# 1. Create an empty priority queue ( or min heap) pq.
# 2. dist[v] = [inf, inf,......inf]
# 3. dist[src] = 0
# 4. Insert all distances to pq.
# 5. While pq is not empty, do the following:
#    u = pq.extract_min()
#    relax all the edges from u that are not in the pq.

from collections import deque

INT_MAX = 4294967295

def addEdge(adj,u,v):
    adj[u].append(v)

def dijkstra(graph, src):
    V = len(graph) # Number of vertices
    dist = [float('inf') for i in range(V)] # To store the shortest distance from source to vertex i.
    dist[src] = 0  # Distance from source to source is 0.
    fin = [False for i in range(V)] # To check if the vertex is finalized or not.

    for count in range(V-1): # V-1 because we need to find the shortest path for V-1 vertices.
        u = -1 # Initialize u to -1
        for i in range(V): # Find the vertex with minimum distance from the source.
            if fin[i]==False and (u==-1 or dist[i]<dist[u]): # If the vertex is not finalized and the distance is less than the minimum distance.
                u=i # Update u to i.
        fin[u] = True # Mark the vertex as finalized.
        for x in range(V): # Relax all the vertices from u.
            if(fin[x]==False and graph[u][x]!=0): # If the vertex is not finalized and the edge is not 0.
                dist[x] = min(dist[x], dist[u]+graph[u][x]) # Update the distance of the vertex.
    return dist 

v = 4 
graph = [[0,5,10,0],[5,0,3,20],[10,3,0,2],[0,20,2,0]]

print(dijkstra(graph,0))