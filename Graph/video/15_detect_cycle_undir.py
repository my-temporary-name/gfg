# Detect Cycle in an Undirected Graph, TC = O(V+E)

# We will use DFS to detect cycle in an undirected graph.
# Idea is to see if adjacent vertex is visited and not parent of current vertex.
# If yes, then cycle is detected.
from collections import deque
INT_MAX = 4294967296

def DFS_Rec(adj, s, visited, parent):
    visited[s] = True # Mark the current vertex as visited
    for u in adj[s]: # For all adjacent vertices of s
        if visited[u] == False: # If u is not visited
            if DFS_Rec(adj,u,visited,s): # Call DFS_Rec function with adjacency list, vertex u and visited list as input
                return True # If cycle is detected, return True
        elif u!= parent: # If u is visited and not parent of current vertex
            return True # Cycle is detected
    return False # If no cycle is detected, return False


def DFS(adj):
    visited = [False]*len(adj)
    for i in range(len(adj)):
        if visited[i]==False:
            if DFS_Rec(adj, i, visited, -1):
                return True
    return False



def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

v = 4 
adj = [[] for i in range(v)]

addEdge(adj,0,1)
addEdge(adj,1,2)
addEdge(adj,2,3)
addEdge(adj,0,2)
addEdge(adj,0,3)
dist =[INT_MAX]*v
dist[0]=0

if(DFS(adj)):
    print("Cycle found")
else:
    print("No cycle")


# Detect Cycle in Directed Graph, TC = O(V+E)
# We need 2 visited lists, one for current DFS traversal and one for global visited list.

from collections import deque
INT_MAX = 4294967296

def DFS_Rec(adj, s, visited, recST):
    visited[s] = True # Mark the current vertex as visited
    recST[s] = True # Mark the current vertex as visited in recST list

    for u in adj[s]: # For all adjacent vertices of s
        if (visited[u]==False and DFS_Rec(adj, u, visited, recST)): # If u is not visited and DFS_Rec function returns True
            return True # Return True
        elif recST[u] == True: # If u is visited in recST list
            return True # Return True
    recST[s] = False # Mark the current vertex as not visited in recST list
    return False # Return False


def DFS(adj):
    visited = [False]*len(adj) # Visited list for current DFS traversal
    recST = [False]*len(adj) # Visited list for global visited list

    for i in range(len(adj)):
        if visited[i]==False:
            if DFS_Rec(adj, i, visited, recST): # Call DFS_Rec function with adjacency list, vertex i and visited list as input
                return True
    return False



def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

v = 6
adj = [[] for i in range(v)]

addEdge(adj,0,1)
addEdge(adj,2,1)
addEdge(adj,2,3)
addEdge(adj,3,4)
addEdge(adj,4,5)
addEdge(adj,5,3)



if(DFS(adj)):
    print("Cycle found")
else:
    print("No cycle")

# What's happening in the above code is that we are using 2 visited lists, one for current DFS traversal and one for global visited list.
# We are marking the current vertex as visited in both visited and recST list.
# If we find a vertex which is visited in recST list, then cycle is detected.
# If we find a vertex which is visited in visited list, then we return True.
# If no cycle is detected, we return False.


# Using Kahn's Algorithm to detect cycle in Directed Graph, TC = O(V+E)
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
            print("There is no cycle: ",*top_order) # Print topological order

g = Graph(6)
g.addEdge(0,1)
g.addEdge(2,1)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(5,3)

print ("Following is a Topological Sort of the given graph")
g.topologicalSort() # call topologicalSort method