# Shortest path in directed acyclic graph in weighted graph, TC = O(V+E)
# We can find the shortest path in a weighted graph using topological sorting.

# shortestPath(adj, s)
# 1. Initialize dist[v] = [Inf, Inf......Inf] for all vertices v
# 2. dist[s] = 0
# 3. find the topological sort of the graph
# 4. For every vertex u in topological sort:
#       a. For every adjacent vertex v of u:
#           if dist[v] > dist[u] + weight(u,v):
#               dist[v] = dist[u] + weight(u,v)


# Python program to find single source shortest paths
# for Directed Acyclic Graphs Complexity :O(V+E)


# Python program to find single source shortest paths
# for Directed Acyclic Graphs Complexity :O(V+E)


from collections import defaultdict

class Graph:
	def __init__(self,vertices):

		self.V = vertices 

		self.graph = defaultdict(list)

	def addEdge(self,u,v,w):
		self.graph[u].append((v,w))


	def topologicalSortUtil(self,v,visited,stack):

		visited[v] = True

		if v in self.graph.keys():
			for node,weight in self.graph[v]:
				if visited[node] == False:
					self.topologicalSortUtil(node,visited,stack)

		stack.append(v)


	def shortestPath(self, s):

		visited = [False]*self.V
		stack =[]

		for i in range(self.V):
			if visited[i] == False:
				self.topologicalSortUtil(s,visited,stack) # Call topologicalSortUtil function that returns topological sort of the graph

		dist = [float("Inf")] * (self.V) # Initialize distances to all vertices as infinite
		dist[s] = 0 # Distance to source vertex is 0

		while stack: # While stack is not empty

			i = stack.pop() # Pop a vertex from stack

			for node,weight in self.graph[i]: # For all adjacent vertices of i
				if dist[node] > dist[i] + weight: # If distance to node is greater than distance to i + weight of edge i->node
					dist[node] = dist[i] + weight # Update distance to node

		for i in range(self.V):
			print (("%d" %dist[i]) if dist[i] != float("Inf") else "Inf" ,end=" ")


g = Graph(6)
g.addEdge(0, 1, 5) # Add edge from 0 to 1 with weight 5
g.addEdge(0, 2, 3) # Add edge from 0 to 2 with weight 3
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)

s = 1

print ("Following are shortest distances from source %d " % s)
g.shortestPath(s)


