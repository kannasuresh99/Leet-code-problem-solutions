class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        
        if k == 0:
            return len(s)

        char_freq = dict()
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        for i, char in enumerate(s):
            if char_freq[char] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i+1:], k)
                return max(left, right)
        
        return len(s)


