#DFS solution
class Solution:
    
    def dfs(self, node, visited, path_visited, adjList):
        visited.add(node)
        path_visited.add(node)
        
        for adj_node in adjList[node]:
            if adj_node not in visited:
                if self.dfs(adj_node, visited, path_visited, adjList):
                    return True
            elif adj_node in path_visited:
                return True
        path_visited.remove(node)
        return False
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        visited = set()
        path_visited = set()
        
        for i in range(V):
            if i not in visited:
                if self.dfs(i, visited, path_visited, adj):
                    return True
                    
        return False

#BFS solution
from collections import deque

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        indegree = [0 for _ in range(V)]
        topo_sort_count = 0
        queue = deque()
        
        for i in range(V):
            for adj_node in adj[i]:
                indegree[adj_node] += 1
                
        for j in range(0, len(indegree)):
            if indegree[j] == 0:
                queue.append(j)
                
        while queue:
            node_ = queue.popleft()
            topo_sort_count += 1
            
            for adj_node in adj[node_]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)
        
        return False if topo_sort_count == V else True

