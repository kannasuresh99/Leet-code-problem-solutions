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

