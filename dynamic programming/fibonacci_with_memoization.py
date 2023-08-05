class Solution:
    def fibonacci(self, n, dp):
        if n <= 1:
            return n
        
        if dp[n]:
            return dp[n]
        
        dp[n] = self.fibonacci(n-1, dp) + self.fibonacci(n-2, dp)

        return dp[n]
    
    def fibonacci_with_tabulation(self, n):
        dp = [None for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
    
    def fibonacci_with_constant_space(self, n):
        a = 0
        b = 1
        
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        
        return c

n = int(input("enter the nth sequence number: "))
dp = [None for _ in range(n+1)]
res = Solution().fibonacci(n, dp)
print(res)
print()
print(Solution().fibonacci_with_tabulation(n))
print()
print(Solution().fibonacci_with_constant_space(n))

