from typing import List

class Solution:
    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, adjList, visited, tin, low, bridges):
        visited.add(node)

        tin[node] = self.timer
        low[node] = self.timer
        self.timer += 1

        for adj_node in adjList[node]:
            if adj_node == parent:
                continue
            if adj_node not in visited:
                self.dfs(adj_node, node, adjList, visited, tin, low, bridges)
                low[node] = min(low[node], low[adj_node])
                #main logic
                if tin[node] < low[adj_node]:
                    bridges.append([node, adj_node])
            else:
                low[node] = min(low[node], low[adj_node])


    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        solving this problem using Tarjan's algorithm
        """
        visited = set()
        tin = [0 for i in range(n)]
        low = [0 for i in range(n)]

        adjList = [[] for _ in range(n)]

        for edge in connections:
            u = edge[0]
            v = edge[1]
            adjList[u].append(v)
            adjList[v].append(u)

        bridges = list()

        self.dfs(0, -1, adjList, visited, tin, low, bridges)

        return bridges
