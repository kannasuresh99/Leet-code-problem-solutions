from typing import List

class Solution:
    def __init__(self):
        self.combinations = []
        self.combo_visited = set()

    def recurse(self, num, n, k, path_arr, path_visited):
        if len(path_arr) == k:
            temp_res = path_arr[:]
            temp_res.sort()
            if tuple(temp_res) not in self.combo_visited:
                self.combinations.append(temp_res)
                self.combo_visited.add(tuple(temp_res))
            return
        
        for i in range(num, n+1):
            if i not in path_visited:
                path_arr.append(i)
                path_visited.add(i)
                self.recurse(i, n, k, path_arr, path_visited)
                path_arr.pop()
                path_visited.remove(i)

        return

    def combine(self, n: int, k: int) -> List[List[int]]:
        for i in range(1, n+1):
            path_arr = [i]
            path_visited = set()
            path_visited.add(i)
            self.recurse(i, n, k, path_arr, path_visited)
        return self.combinations