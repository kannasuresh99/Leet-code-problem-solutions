class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        if n <= 1:
            return n
        c = 0
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        
        return c