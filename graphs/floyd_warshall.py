class Solution:
    def shortest_distance(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = float('inf')
                if i==j:
                    matrix[i][j] = 0
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][via]+matrix[via][j]<matrix[i][j]:
                        matrix[i][j] = matrix[i][via]+matrix[via][j]
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = -1
