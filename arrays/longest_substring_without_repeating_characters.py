"""
question link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        hashmap = {}
        longest_substr_len = 0

        while r < len(s):
            if s[r] in hashmap:
                l = max(hashmap[s[r]]+1, l)
            hashmap[s[r]] = r
            longest_substr_len = max(longest_substr_len, r-l+1)
            r += 1
        return longest_substr_len

