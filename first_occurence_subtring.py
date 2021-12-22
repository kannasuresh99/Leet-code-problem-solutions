#my solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        if needle == "":
            return 0
        else:
            if needle in haystack:
                for i in range(0,len(haystack)):
                    substring = haystack[i:needle_len+i]
                    if substring == needle:
                        return i
            else:
                return -1
        

res = Solution()
result = res.strStr(haystack="bobbub",needle="bbu")
print(result)