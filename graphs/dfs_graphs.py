class Solution:
    def dfs(self, visited, node, adj, res):
        visited.add(node)
        res.append(node)
        
        for node_ in adj[node]:
            if node_ not in visited:
                self.dfs(visited, node_, adj, res)

    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        res = []
        visited = set()
        self.dfs(visited, 0, adj, res)
        return res