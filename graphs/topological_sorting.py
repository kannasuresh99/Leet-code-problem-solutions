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

#BFS solution
#Kahn's algorithm

from collections import deque

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        indegree = [0 for _ in range(V)]
        ans = list()
        queue = deque()
        
        for i in range(V):
            for adj_node in adj[i]:
                indegree[adj_node] += 1
                
        for j in range(0, len(indegree)):
            if indegree[j] == 0:
                queue.append(j)
                
        while queue:
            node_ = queue.popleft()
            ans.append(node_)
            
            for adj_node in adj[node_]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)
        
        return ans

