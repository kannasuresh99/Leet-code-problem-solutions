"""question link: https://leetcode.com/problems/powx-n/"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        calculate ans only when n%2 is odd
        else just multiply the x with itself
        """
        new_n = n
        ans = 1.0
        if new_n < 0:
            new_n = -1*new_n
        
        while new_n > 0:
            if new_n % 2 == 1:
                ans *= x
                new_n -= 1
            else:
                x *= x
                new_n = new_n // 2
        
        if n < 0:
            return 1/ans
        return ans

