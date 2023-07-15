from collections import deque
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
    
#BFS solution Topological sorting
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adjRev = [[] for _ in range(len(graph))]
        topo_sort = []
        
        for i in range(len(graph)):
            for adj_node in graph[i]:
                adjRev[adj_node].append(i)
        
        indegree = [0 for d in range(len(graph))]
        
        for j in range(len(graph)):
            for adj_node in adjRev[j]:
                indegree[adj_node] += 1
        
        queue = deque()
        
        for k in range(0, len(indegree)):
            if indegree[k] == 0:
                queue.append(k)
                
        
        while queue:
            node_ = queue.popleft()
            topo_sort.append(node_)
            
            for adj_node in adjRev[node_]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)
                    
        topo_sort.sort()
        
        return topo_sort
