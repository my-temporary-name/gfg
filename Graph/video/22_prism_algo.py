# Prism algo implementation:

# I/P: graph[][]
# [[0, 5, 8, 0],
#  [5, 0, 10, 15],
#  [8, 10, 0, 20],
#  [0, 15, 20, 0]]
# O/P: 0-1: 5
#      0-2: 8
#      1-3: 15
# Total cost: 28

# Idea of Prism algo is to find the minimum weight edge from the set of edges that connect the two sets of vertices, 
# one set contains the vertices already included in MST and the other set contains the vertices not yet included.
# TC = O(V^2)

import sys
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for i in range(vertices)]

    def printMST(self, parent):
        print("Edge\tWeight")
        for i in range(1,self.V):
            print(parent[i],"-",i,"\t",self.graph[i][parent[i]])
    

    def minKey(self,key, mstSet):
        min = sys.maxsize
        for v in range(self.V):
             if key[v]<min and mstSet[v]==False:
                 min = key[v]
                 min_index = v
        return min_index
    
    def primMST(self):
        key = [sys.maxsize]*self.V
        parent = [None]*self.V 
        key[0]=0
        mstSet = [False]*self.V

        parent[0]=-1

        for cout in range(self.V):       
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.printMST(parent)

     
if __name__ == '__main__':
	g = Graph(5)
	g.graph = [[0, 2, 0, 6, 0],
			[2, 0, 3, 8, 5],
			[0, 3, 0, 0, 7],
			[6, 8, 0, 0, 9],
			[0, 5, 7, 9, 0]]

	g.primMST()
# Idea for better implementation:
# 1. Use adjacency list to represent the graph.
# 2. Use minHeap to store the edges.
# Try coding the above idea.
# TC =(E logV)