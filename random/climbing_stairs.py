class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        if n == 1:
            return 1
        for value in range(0,n-1):
            sum = a + b
            a = b
            b = sum

        return sum

res = Solution()
result = res.climbStairs(5)
print(result)