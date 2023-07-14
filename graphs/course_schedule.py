from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #if there's a cyclic dependency you can't complete all courses
        #so here we use BFS topo sort to find whether there's a cycle

        #creating adjacency list
        adjList = [[] for _ in range(numCourses)]
        queue = deque()
        topo_sort = list()

        for u,v in prerequisites:
            adjList[v].append(u)

        indegree = [0 for deg in range(numCourses)]

        for i in range(numCourses):
            for adj_node in adjList[i]:
                indegree[adj_node] += 1
        
        for j in range(0, len(indegree)):
            if indegree[j] == 0:
                queue.append(j)

        while queue:
            node_ = queue.popleft()
            topo_sort.append(node_)

            for adj_node in adjList[node_]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)

        return True if len(topo_sort) == numCourses else False

