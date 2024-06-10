# Kosaraju's Algorithm
# This algorithm is used to find the strongly connected components in a graph.
# Components are strongly connected if there is a path between each pair of vertices.

# 1. Order the vertices in decreasing order of their finishing time in DFS.
# 2. Reverse all the edges of the graph.
# 3. Do DFS of the reversed graph in the order obtained in step 1.
#    For every vertex, print all the reachable vertices as one strongly connected component.

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Implementation:
# Step 1:
# 1. create an empty stack st.
# 2. For every vertex u, do the following:
#   if u is not visited, then do DFS_Recurse(u,st).
# 3. While (st is not empty), pop an item and add to result list.

# DFS_Recurse(u,st):
# 1. Mark u as visited.
# 2. For every adjacent v, if v is not visited, then do DFS_Recurse(v,st).
# 3. Push u to stack st.


from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list) # Adjacency list to store the graph.
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def _dfs(self, v, visited, stack): # Helper function to do DFS. (Step 1)
        visited[v]=True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited, stack)
        stack.append(v)
    
    def _transpose(self): # Helper function to reverse the graph. (Step 2)
        transposed_graph = Graph(self.V)
        for node in self.graph:
            for neighbor in self.graph[node]:
                transposed_graph.add_edge(neighbor, node)
        return transposed_graph

    def _fill_order(self,visited, stack): # Helper function to fill the stack. (Step 1)
        for i in range(self.V):
            if not visited[i]:
                self._dfs(i, visited, stack)
    
    def _dfs_util(self, v, visited, components): # Helper function to do DFS. (Step 3)
        visited[v] = True
        components.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self._dfs_util(neighbor, visited, components)
    
    def kosaraju_scc(self): # Main function to find the strongly connected components.
        stack = deque()
        visited = [False]*self.V

        self._fill_order(visited, stack)

        transposed_graph = self._transpose()

        visited = [False]*self.V
        scc_list = []
        while stack:
            node = stack.pop()
            if not visited[node]:
                components = []
                transposed_graph._dfs_util(node,visited, components)
                scc_list.append(components)
        
        return scc_list

# Example usage
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    sccs = g.kosaraju_scc()
    print("Strongly Connected Components:", sccs)