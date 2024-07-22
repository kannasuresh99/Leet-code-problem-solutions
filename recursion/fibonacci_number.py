"""
question link: https://leetcode.com/problems/fibonacci-number/
"""

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1)+self.fib(n-2)
    
res = Solution().fib(10)
print(res)