# 1. Directed and Undirected Graphs
# If i write (V1, V2) in a graph, it means there is a directed edge from V1 to V2.

# Directed graph is used by crawlers to crawl web pages. It is also used in social networks like Facebook, Twitter, etc.

# Indegree of a vertex is the number of edges coming into it. 
# Outdegree of a vertex is the number of edges going out of it.
# sum of indegree of all vertices = sum of outdegree of all vertices = number of edges in the graph. = 2 * number of edges in an undirected graph. (inundirected graph, there is an edge between two vertices, so it is counted twice)

# Maximum number of edges in a directed graph with n vertices = n(n-1)
# Maximum number of edges in an undirected graph with n vertices = n(n-1) / 2

# Walk: A walk is a sequence of vertices and edges in a graph. A walk is closed if the starting vertex is the same as the ending vertex.
# Path: A path is a walk in which all vertices are distinct.
# Cycle: A cycle is a closed path in which all vertices are distinct except the starting and ending vertices.
# Acyclic graph: A graph with no cycles is called an acyclic graph.

# DAG: Directed Acyclic Graph

# Weighted Graph: A graph in which each edge has a weight associated with it.

# Graph representation:
# 1. Adjacency matrix
# 2. Adjacency list

# Adjacency matrix:
# 1. It is a 2D array of size V x V where V is the number of vertices in the graph.
# 2. Let the 2D array be adj[][], a slot adj[i][j] = 1 indicates that there is an edge from vertex i to vertex j. (in case of directed graph)
# 3. Adjacency matrix for undirected graph is always symmetric.
# Example:
# 0 1 0
# 0 0 1
# 1 0 0
# The above is an adjacency matrix representation for the graph: 0 -> 1 -> 2 -> 0

# How to handle vertices with arbitrary names?
# We use array indexes to represent them. We can use a hash table to map the vertex names to indexes. # hash table can do this mapping in O(1) time.
# ex: hash table: {A: 0, B: 1, C: 2}


# Space required for adjacency matrix: O(VxV)
# Operations:
# 1. check if u and v are adjacent: O(1)
# 2. Find all adjacent vertices of a vertex: O(V)
# 3. Find degree of a vertex: O(V)
# 4. Add or Remove an edge: O(1)
# 5. Add or Remove a vertex: O(V^2)

# Problem with adjacency matrix:
# 1. Space: O(V^2). For sparse graphs, this is a huge waste of space.
# 2. Iterating over all edges takes O(V^2) time.

# Adjacency list:
# 1. An array of lists is used. The size of the array is equal to the number of vertices.
# 2. Let the array be array[]. An entry array[i] represents the list of vertices adjacent to the ith vertex.
# Example:
#     1
#   /  |  3
#  /   | /
# 0----2

# 0: 1, 2
# 1: 0, 2
# 2: 0, 1, 3
# 3: 2
# Above is an adjacency list representation of the graph.

# Most Popular representation of adjacency list is a a) Dynamic array b) Linked list


# In case of Directed graph
#          1
#        ^  ^ ^
#       /   |  \
#      0    |   3
#       \   |   ^
#        v  v  / 
#           2

# 0: 1 -> 2
# 1: 2
# 2: 3 -> 1
# 3: 1

# Space: O(V+E)
# Operations:
# 1. Check if there's an edge between u and v: O(V)
# 2. Find all adjacent vertices of a vertex: O(degree of the vertex)
# 3. Find the degree of a vertex: O(1)
# 4. Add or Remove an edge: O(V)
# 5. Add or Remove a vertex: O(V+E)


# Comparison:
#                                         Adjacency List    Adjacency Matrix
# Space:                                     O(V+E)            O(V^2)
# Check edge between u and v:                  O(V)              O(1)
# Find all adjacent vertices of a vertex:  O(degree of vertex)    O(V)
# Add an Edge:                                 O(1)              O(1)
# Remove an Edge:                              O(V)              O(1)

# In general Adjacency List is much more efficient in most of the cases.

