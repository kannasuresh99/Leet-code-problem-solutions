#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        left = 0
        right = 0
        char_set = set()
        char_freq = dict()
        max_count = -1
        
        while right < len(s):
            while right < len(s) and len(char_set) <= k:
                char_set.add(s[right])
                char_freq[s[right]] = char_freq.get(s[right], 0) + 1
                if len(char_set) == k:
                    max_count = max(max_count, right-left+1)
                right += 1
            char_freq[s[left]] -= 1
            if char_freq[s[left]] == 0:
                char_set.remove(s[left])
            left += 1
        
        return max_count
                
