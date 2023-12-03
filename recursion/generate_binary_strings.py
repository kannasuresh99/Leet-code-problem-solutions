class Solution:
    def recurse(self, idx: int, n: int, rec_arr: list, res: list):
        if idx == n:
            res.append("".join(rec_arr))
            return
        
        rec_arr.append("0")
        self.recurse(idx+1, n, rec_arr, res)
        rec_arr.pop()
        
        rec_arr.append("1")
        self.recurse(idx+1, n, rec_arr, res)
        rec_arr.pop()
        
        return

    def generate_binary_strings(self, n: int):
        res = []
        self.recurse(0, n, [], res)
        for binary_str in res:
            print(binary_str)
        
Solution().generate_binary_strings(n=5)
