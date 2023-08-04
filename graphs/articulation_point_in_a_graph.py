#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    def __init__(self):
        self.timer = 1
        
    def dfs(self, node, parent, tin, low, visited, adj, mark):
        visited.add(node)
        
        tin[node] = self.timer
        low[node] = self.timer
        self.timer += 1
        child = 0
        for adj_node in adj[node]:
            if adj_node == parent:
                continue
            if adj_node not in visited:
                self.dfs(adj_node, node, tin, low, visited, adj, mark)
                low[node] = min(low[node], low[adj_node])
                
                if low[adj_node] >= tin[node] and parent != -1:
                    mark[node] = True
                child += 1
            else:
                #this step different than bridges problem
                low[node] = min(low[node], tin[adj_node])
        
        if child > 1 and parent == -1:
            mark[node] = True

    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        # code here
        tin = [0 for _ in range(V)]
        low = [0 for _ in range(V)]
        visited = set()
        mark = [False for _ in range(V)]
        articulation_points = []
        
        for i in range(V):
            if i not in visited:
                self.dfs(i, -1, tin, low, visited, adj, mark)
                
        
        for i in range(V):
            if mark[i] == True:
                articulation_points.append(i)
        
        if len(articulation_points) == 0:
            return [-1]
            
        return articulation_points
        
