"""
question link: https://leetcode.com/problems/generate-parentheses/
"""

class Solution:
    def recurse(self, idx: int, n: int, rec_arr: list, parenthesis_count: dict, res:list):
        if idx == 2*n:
            res.append("".join(rec_arr))
            return
        
        if parenthesis_count["("] < n:
            rec_arr.append("(")
            parenthesis_count["("] += 1
            self.recurse(idx+1, n, rec_arr, parenthesis_count, res)
            rec_arr.pop()
            parenthesis_count["("] -= 1
        
        if parenthesis_count[")"] < parenthesis_count["("]:
            rec_arr.append(")")
            parenthesis_count[")"] += 1
            self.recurse(idx+1, n, rec_arr, parenthesis_count, res)
            rec_arr.pop()
            parenthesis_count[")"] -= 1
        
        return

    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        parenthesis_count = {"(": 0, ")": 0}
        self.recurse(0, n, [], parenthesis_count, res)
        return res

res = Solution().generateParenthesis(5)
print(res)