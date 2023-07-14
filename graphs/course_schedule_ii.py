from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        result = list()

        adjList = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adjList[v].append(u)

        indegree = [0 for d in range(numCourses)]

        for i in range(numCourses):
            for adj_node in adjList[i]:
                indegree[adj_node] += 1

        for j in range(len(indegree)):
            if indegree[j] == 0:
                queue.append(j)

        while queue:
            node_ = queue.popleft()
            result.append(node_)

            for adj_node in adjList[node_]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)

        return result if len(result) == numCourses else []