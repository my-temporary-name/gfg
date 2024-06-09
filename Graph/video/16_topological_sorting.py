# Topological Sorting (Kahn's BFS based algorithm), TC = O(V+E)
# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u v,
# vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

# BFS Based Solution:
# 1. Store indegree of each vertex.
# 2. Create a queue ,q
# 3. Add all 0 indegree vertices to q
# 4. While q is not empty:
#    a. u = q.pop()
#    b. print u
#    c. For all adjacent vertices v of u:
#       i.  reduce indegree of v by 1
#       ii. if indegree of v becomes 0, add v to q

# Initially push 0 indegree vertices to queue

from collections import defaultdict

class Graph: # Class to represent a graph
    def __init__(self,vertices): # Constructor
        self.graph = defaultdict(list) # Default dictionary to store graph
        self.V = vertices # No. of vertices
    
    def addEdge(self,u,v): # Function to add an edge to graph
        self.graph[u].append(v)
    
    def topologicalSort(self): # Function to print Topological Sort of graph

        in_degree = [0]*(self.V) # Create a vector to store indegrees of all vertices

        for i in self.graph: # Traverse adjacency lists to fill indegrees of vertices
            for j in self.graph[i]: # Traverse adjacency lists of all vertices
                in_degree[j]+=1 # Increment indegree of j by 1
        queue = [] # Create a queue to store all vertices with indegree 0
        for i in range(self.V): # Traverse indegree list 
            if in_degree[i] == 0: # If indegree of vertex i is 0
                queue.append(i) # Push vertex i to queue
        
        cnt = 0 # Initialize count of visited vertices

        top_order = [] # Store topological order

        while queue: # While queue is not empty
            u = queue.pop(0) # Pop vertex from queue and print it
            top_order.append(u) # Append vertex to top_order

            for i in self.graph[u]: # Iterate over all adjacent vertices of vertex u
                in_degree[i] -=1 # Reduce indegree of adjacent vertices by 1
                if in_degree[i] == 0: # If indegree of adjacent vertex i becomes 0
                    queue.append(i) # Push vertex i to queue
            cnt +=1 # Increment count of visited vertices
        if cnt != self.V: # Check if count of visited vertices is not equal to total number of vertices
            print ("There exists a cycle in the graph")
        else:
            print(*top_order) # Print topological order

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print ("Following is a Topological Sort of the given graph")
g.topologicalSort() # call topologicalSort method


# Topological Sort using DFS, TC = O(V+E)
# 1. Create a stack, st
# 2. For every vertex u, do following:
#    a. If u is not visited:
#        DFS(u,st)
#while st is not empty:
#    print st.pop()
# -------------------------------
# DFS(u,st):
# 1. Mark u as visited
# 2. For all adjacent vertices v of u:
#    a. If v is not visited:
#        DFS(v,st)
# 3. Push u to stack

from collections import defaultdict

class Graph: # Class to represent a graph
    def __init__(self,vertices): # Constructor
        self.graph = defaultdict(list) # Default dictionary to store graph
        self.V = vertices # No. of vertices
    
    def addEdge(self,u,v): # Function to add an edge to graph
        self.graph[u].append(v)
    
    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i]==False:
                self.topologicalSortUtil(i, visited, stack)
        stack.append(v)
    
    def topologicalSort(self):
        visited = [False]*self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
        print(*stack[::-1])


# Driver Code
if __name__ == '__main__':
	g = Graph(6)
	g.addEdge(5, 2)
	g.addEdge(5, 0)
	g.addEdge(4, 0)
	g.addEdge(4, 1)
	g.addEdge(2, 3)
	g.addEdge(3, 1)

	print("Following is a Topological Sort of the given graph")

	# Function Call
	g.topologicalSort()