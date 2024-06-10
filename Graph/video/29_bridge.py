# Bridges in a graph
# A bridge (or cut-edge) is an edge in an undirected graph whose removal increases the number of connected components.
# low[i] is lowest reachable discovery time from i
# disc[i] is the discovery time of i
# Bridge is an edge (u, v) such that low[v] > disc[u]

# Python program to find bridges in a given undirected graph
#Complexity : O(V+E)

from collections import defaultdict

class Graph:

	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
		self.Time = 0

	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def bridgeUtil(self,u, visited, parent, low, disc):

		visited[u]= True

		disc[u] = self.Time
		low[u] = self.Time
		self.Time += 1

		for v in self.graph[u]:

			if visited[v] == False :
				parent[v] = u
				self.bridgeUtil(v, visited, parent, low, disc)

				low[u] = min(low[u], low[v])

				if low[v] > disc[u]:
					print ("%d %d" %(u,v))
	
					
			elif v != parent[u]: # Update low value of u for parent function calls.
				low[u] = min(low[u], disc[v])


	def bridge(self):

		visited = [False] * (self.V) # Mark all the vertices as not visited
		disc = [float("Inf")] * (self.V) # Initialize discovery time and low value
		low = [float("Inf")] * (self.V) # Initialize discovery time and low value
		parent = [-1] * (self.V) # Initialize parent

		for i in range(self.V):
			if visited[i] == False:
				self.bridgeUtil(i, visited, parent, low, disc)
		

g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)


print ("Bridges in first graph ")
g1.bridge()

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print ("\nBridges in second graph ")
g2.bridge()

