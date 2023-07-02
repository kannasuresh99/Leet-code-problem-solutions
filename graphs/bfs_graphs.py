from typing import List
from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        visited = set()
        queue = deque([0])
        visited.add(0)
        bfs = []
        
        while queue:
            num = queue.popleft()
            bfs.append(num)
            for adj_node in adj[num]:
                if adj_node not in visited:
                    queue.append(adj_node)
                    visited.add(adj_node)
                    
        return bfs