"""
question link: https://www.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1
"""

class Solution:
    def sumOfDivisors(self, N):
        sum = 0
        for i in range(1, N + 1):
            sum += (N // i) * i
        return sum