#User function Template for python3

from typing import List

class Solution:
    def dfs(self, node, visited, adjList, stack):
        visited.add(node)
        
        for adj_node in adjList[node]:
            if adj_node[0] not in visited:
                self.dfs(adj_node[0], visited, adjList, stack)
        
        stack.append(node)

    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        visited = set()
        stack = []
        adjList = [[] for _ in range(n)]
        dist = [float('inf') for d in range(n)]
        
        for i in range(m):
            u = edges[i][0]
            v = edges[i][1]
            wt = edges[i][2]
            adjList[u].append([v, wt])
            
        for j in range(n):
            if j not in visited:
                self.dfs(j, visited, adjList, stack)
                
        dist[0] = 0
        
        while stack:
            node_ = stack.pop()
            
            for adj_node in adjList[node_]:
                adj_node_val = adj_node[0]
                adj_node_wt = adj_node[1]
                if dist[node_] + adj_node_wt < dist[adj_node_val]:
                    dist[adj_node_val] = dist[node_] + adj_node_wt
        
        for x in range(len(dist)):
            if dist[x] == float('inf'):
                dist[x] = -1
        
        return dist
        
