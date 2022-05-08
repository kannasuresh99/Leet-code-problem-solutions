class Solution:
    def orangesRotting(self, grid):
        q = []
        fresh = 0
        time = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(0, rows):
            for col in range(0, cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append([row, col])

        directions = [[0,1], [0, -1], [-1, 0], [1, 0]]
        while fresh > 0 and q:
            for i in range(0, len(q)):
                r, c = q.pop(0)
                for direction in directions:
                    row = r + direction[0]
                    col = c + direction[1]
                    if (row < 0 or row == len(grid)) or (col < 0 or col == len(grid[0])
                    or (grid[row][col] != 1)):
                        continue
                    else:
                        grid[row][col] = 2
                        q.append([row, col])
                        fresh -= 1
            time += 1
        time = -1 if fresh > 0 else time
        return time
res = Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
print(res)