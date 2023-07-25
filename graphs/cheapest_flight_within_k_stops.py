from collections import deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #dijkstra implementation with queue
        queue = deque()

        adjList = [[] for _ in range(n)]

        for edge in flights:
            u = edge[0]
            v = edge[1]
            wt = edge[2]
            adjList[u].append([v, wt])

        queue.append([0, src, 0])

        prices = [float('inf') for d in range(n)]
        prices[src] = 0

        while queue:
            stops, node, dist = queue.popleft()

            for adj_node, wt in adjList[node]:
                if stops < k+1:
                    if dist + wt < prices[adj_node]:
                        prices[adj_node] = dist + wt
                        queue.append([stops+1, adj_node, prices[adj_node]])

        return prices[dst] if prices[dst] != float('inf') else -1
