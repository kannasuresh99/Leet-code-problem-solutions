"""
The below code uses sqrt(n) time complexity to check if a number is prime or not.
"""

class Solution:
    def is_prime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True

        factors = 0
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                factors += 1
                if n//i != i:
                    factors += 1

        return True if factors == 2 else False
    
# Time complexity: O(sqrt(n))
# Space complexity: O(1)
    
sol = Solution()
print(sol.is_prime(19))