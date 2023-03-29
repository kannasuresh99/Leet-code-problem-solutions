class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, k):
            if k == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols
                or (r,c) in path or board[r][c] != word[k]):
                return False

            path.add((r,c))
            res = (dfs(r+1, c, k+1) or
                    dfs(r-1, c, k+1) or
                    dfs(r, c+1, k+1) or
                    dfs(r, c-1, k+1))
            path.remove((r,c))
            return res


        for i in range(0, rows):
            for j in range(0, cols):
                if dfs(i, j, 0):
                    return True
        return False