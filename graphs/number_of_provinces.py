from collections import defaultdict
from typing import List


class Solution:
    def dfs(self, node, visited, adjList):
        visited.add(node)
        for node_ in adjList[node]:
            if node_ not in visited:
                self.dfs(node_, visited, adjList)
        return

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        adjList = defaultdict(list)
        num_of_provinces = 0

        for i in range(0, len(isConnected)):
            for j in range(0, len(isConnected[i])):
                if isConnected[i][j] != 0:
                    adjList[i].append(j)
        
        for i in range(len(isConnected)):
            if i not in visited:
                self.dfs(i, visited, adjList)
                num_of_provinces += 1
        
        return num_of_provinces