class Solution:
    def findPath(self, m, n):
        # code here
        result = []
        visited = set()
        def Recurse(i, j, str_arr):
            if i == n-1 and j == n-1:
                result.append("".join(str_arr))
                return
            
            if (i+1<n) and (tuple([i+1,j]) not in visited) and (m[i+1][j] == 1):
                str_arr.append("D")
                visited.add(tuple([i, j]))
                Recurse(i+1, j, str_arr)
                str_arr.pop()
                visited.remove(tuple([i, j]))
                
            if (j-1>=0) and (tuple([i,j-1]) not in visited) and (m[i][j-1] == 1):
                str_arr.append("L")
                visited.add(tuple([i, j]))
                Recurse(i, j-1, str_arr)
                str_arr.pop()
                visited.remove(tuple([i, j]))
                
            if (j+1<n) and (tuple([i,j+1]) not in visited) and (m[i][j+1] == 1):
                str_arr.append("R")
                visited.add(tuple([i, j]))
                Recurse(i, j+1, str_arr)
                str_arr.pop()
                visited.remove(tuple([i, j]))
                
            if (i-1>=0) and (tuple([i-1,j]) not in visited) and (m[i-1][j] == 1):
                str_arr.append("U")
                visited.add(tuple([i, j]))
                Recurse(i-1, j, str_arr)
                str_arr.pop()
                visited.remove(tuple([i, j]))
                
            return
        if m[0][0] == 1:
            Recurse(0,0,[])
        return result

res = Solution().findPath([[1, 0, 0, 0],
                            [1, 1, 0, 1], 
                            [1, 1, 0, 0],
                            [0, 1, 1, 1]], 4)

print(res)