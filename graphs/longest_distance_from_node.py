class Solution:
    def dfs(self, node, visited, dist, adjList, max_dist):
        visited.add(node)

        for adj_node, wt in adjList[node]:
            if adj_node not in visited:
                max_dist = self.dfs(adj_node, visited, dist+wt, adjList, max(max_dist, dist+wt))
                
        return max_dist
        


    def findMax(self, edges, n, q, query):
        #create adjacency list
        adjList = [[] for _ in range(n+1)]
        res = list()
        
        for edge in edges:
            u = edge[0]
            v = edge[1]
            wt = edge[2]
            adjList[u].append([v, wt])
            adjList[v].append([u, wt])
            
        for node in query:
            visited = set()
            max_dist_of_node = self.dfs(node, visited, 0, adjList, float('-inf'))
            res.append(max_dist_of_node)
        
        return res
    
res = Solution().findMax([[1, 5, 3],
             [2, 5, 3],
             [1, 4, 2],
             [5, 3, 2]], 5, 4, [1, 3, 4, 5])

print(res)