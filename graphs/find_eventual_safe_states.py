from typing import List


class Solution:
    def dfs(self, node, visited, path_visited, check, graph):
        visited.add(node)
        path_visited.add(node)

        for adj_node in graph[node]:
            if adj_node not in visited:
                if self.dfs(adj_node, visited, path_visited, check, graph):
                    return True
            elif adj_node in path_visited:
                return True
        
        path_visited.remove(node)
        check[node] = 1
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        path_visited = set()
        check = [0 for i in range(len(graph))]
        safe_nodes = []

        for i in range(0, len(graph)):
            if i not in visited:
                self.dfs(i, visited, path_visited, check, graph)

        for j in range(0, len(graph)):
            if check[j] == 1:
                safe_nodes.append(j)

        return safe_nodes