"""
question link: https://leetcode.com/problems/count-good-numbers/
"""

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        #no of even places
        if n % 2 == 0:
            num_of_even = n//2
        else:
            num_of_even = (n + 1)//2
        
        #no of odd places
        num_of_odd = n//2

        even_combo = pow(5, num_of_even, MOD)
        prime_combo = pow(4, num_of_odd, MOD)

        return (even_combo*prime_combo)%MOD


        