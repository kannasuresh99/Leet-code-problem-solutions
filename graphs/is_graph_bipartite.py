from collections import deque
from typing import List

#BFS solution

class Solution:
    def bfs(self, node, graph, is_colored_map):
        queue = deque()
        queue.append(node)
        colors_dict = {0:1, 1:0}
        is_colored_map[node] = 0

        while queue:
            node = queue.popleft()
            current_node_color = is_colored_map[node]
            
            for adj_node in graph[node]:
                if adj_node not in is_colored_map:
                    queue.append(adj_node)
                    is_colored_map[adj_node] = colors_dict[current_node_color]
                elif current_node_color == is_colored_map[adj_node]:
                    return False

        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        is_colored_map = dict()
        
        for i in range(0, len(graph)):
            if i not in is_colored_map:
                if not self.bfs(i, graph, is_colored_map):
                    return False

        return True

        