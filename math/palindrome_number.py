"""
question link: https://leetcode.com/problems/palindrome-number/
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_num = x
        rev_num = 0
        if x < 0:
            return False

        while x > 0:
            num_to_add = x % 10
            rev_num = (rev_num*10) + num_to_add
            x = x // 10
        
        return True if rev_num == original_num else False