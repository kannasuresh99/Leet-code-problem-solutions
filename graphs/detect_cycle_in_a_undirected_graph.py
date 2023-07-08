from typing import List
from collections import deque

#BFS solution
class Solution:
    def detect_cycle(self, node, visited, adjList):
        visited.add(node)
        queue = deque()
        queue.append([node, -1])
        
        while queue:
            node_, parent = queue.popleft()
            
            for neighbor_node in adjList[node_]:
                if neighbor_node not in visited:
                    visited.add(neighbor_node)
                    queue.append([neighbor_node, node_])
                elif neighbor_node in visited and neighbor_node != parent:
                    return True
        
        return False

    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        visited = set()
        for i in range(V):
            if i not in visited:
                if self.detect_cycle(i, visited, adj) == True:
                    return True
        
        return False
    

#DFS solution


class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        vis = [False]*V

        def dfs(v, vis, adj, parent):
            vis[v] = True
            for neighbour in adj[v]:
                if not vis[neighbour]:
                    if dfs(neighbour, vis, adj, v):
                        return True
                elif parent != neighbour:
                    return True
            return False
        for v in range(V):
            if not vis[v]:
                if dfs(v, vis, adj, -1):
                    return True
        return False
