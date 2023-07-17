#User function Template for python3
from collections import deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        #creating adjacency list
        adjList = [[] for _ in range(n)]
        queue = deque()
        
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
            
        dist = [float('inf') for d in range(n)]
        
        dist[src] = 0
        
        queue.append(src)
        
        while queue:
            node_ = queue.popleft()
            
            for adj_node in adjList[node_]:
                if dist[node_] + 1 < dist[adj_node]:
                    dist[adj_node] = dist[node_] + 1
                    queue.append(adj_node)
        
        for idx, num in enumerate(dist):
            if dist[idx] == float('inf'):
                dist[idx] = -1
        
        return dist
        
