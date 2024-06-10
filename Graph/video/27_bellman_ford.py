# Bellman Ford Algorithm, O(VE) for adjacency list.
# Bellman Ford algorithm is used to find the shortest path from the source vertex to all other vertices in the graph.
# It also detects negative weight cycles in the graph.
# Idea is to relax all the edges V-1 times, where V is the number of vertices in the graph.

# We process all the edges V-1 times, because the shortest path can have at most V-1 edges.

class Graph:

	def __init__(self, vertices):
		self.V = vertices # No. of vertices
		self.graph = []

	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	def printArr(self, dist):
		print("Vertex Distance from Source")
		for i in range(self.V):
			print("{0}\t\t{1}".format(i, dist[i]))

	def BellmanFord(self, src):

		dist = [float("Inf")] * self.V
		dist[src] = 0

		for _ in range(self.V - 1): # Relax all the edges V-1 times.
			for u, v, w in self.graph: # Relax all the edges.
				if dist[u] != float("Inf") and dist[u] + w < dist[v]: # If the distance of u is not infinity and the distance of u + weight is less than the distance of v.
					dist[v] = dist[u] + w  # Update the distance of v.


		for u, v, w in self.graph: # Check for negative weight cycle.
			if dist[u] != float("Inf") and dist[u] + w < dist[v]: # If the distance of u is not infinity and the distance of u + weight is less than the distance of v.
				print("Graph contains negative weight cycle")
				return

		self.printArr(dist)


# Driver's code
if __name__ == '__main__':
	g = Graph(5)
	g.addEdge(0, 1, -1)
	g.addEdge(0, 2, 4)
	g.addEdge(1, 2, 3)
	g.addEdge(1, 3, 2)
	g.addEdge(1, 4, 2)
	g.addEdge(3, 2, 5)
	g.addEdge(3, 1, 1)
	g.addEdge(4, 3, -3)

	# function call
	g.BellmanFord(0)