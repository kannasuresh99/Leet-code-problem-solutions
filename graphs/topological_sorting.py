#DFS solution
class Solution:
    def dfs(self, node, adjList, visited, stack):
        visited.add(node)
        
        for adj_node in adjList[node]:
            if adj_node not in visited:
                self.dfs(adj_node, adjList, visited, stack)
                
        stack.append(node)
        
    
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        visited = set()
        stack = list()
        ans = list()
        
        for i in range(V):
            if i not in visited:
                self.dfs(i, adj, visited, stack)
                
        
        while stack:
            ans.append(stack.pop())
        
        return ans

