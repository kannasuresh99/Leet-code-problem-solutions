from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        #creating adjacency matrix
        adjMatrix = []
        for i in range(n):
            mat = []
            for j in range(n):
                if i == j:
                    mat.append(0)
                else:
                    mat.append(float('inf'))
            adjMatrix.append(mat)
        
        for edge in edges:
            adjMatrix[edge[0]][edge[1]] = edge[2]
            adjMatrix[edge[1]][edge[0]] = edge[2]

        #implementing floyd-warshall algorithm
        for via in range(n):
            for row in range(n):
                for col in range(n):
                    if adjMatrix[row][via] == float('inf') or adjMatrix[via][col] == float('inf'):
                        continue
                    adjMatrix[row][col] = min(adjMatrix[row][col], adjMatrix[row][via]+adjMatrix[via][col])

        #core logic
        city_count = n
        city_number = -1

        for i in range(n):
            cnt = 0
            for j in range(n):
                if adjMatrix[i][j] <= distanceThreshold:
                    cnt += 1
            if cnt <= city_count:
                city_count = cnt
                city_number = i

        return city_number

