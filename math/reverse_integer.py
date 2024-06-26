"""
question link: https://leetcode.com/problems/reverse-integer/
"""

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        rev_num = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x > 0:
            num_to_add = x % 10
            if rev_num >= (INT_MAX-num_to_add) / 10:
                return 0
            rev_num = (rev_num*10) + num_to_add
            x = x // 10
        return sign*rev_num