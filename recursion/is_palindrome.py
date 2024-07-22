"""
question link: https://leetcode.com/problems/valid-palindrome/
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        all_alphabets = set('abcdefghijklmnopqrstuvwxyz0123456789')
        def recurse(start, end):
            if start >= end:
                return True
            while start < end and s[start] not in all_alphabets:
                start += 1
            while start < end and s[end] not in all_alphabets:
                end -= 1
            if s[start] == s[end]:
                return recurse(start+1, end-1)
            else:
                return False
        return recurse(0, len(s)-1)
                
