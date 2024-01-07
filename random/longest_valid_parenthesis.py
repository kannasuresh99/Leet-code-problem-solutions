class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0
        while len(s) > 1:
            atleast_one_valid = False
            length = 0
            for i in range(0, len(s)-1):
                if s[i] == '(' and s[i+1] == ')':
                    length += 2
                    s = s[0:i] + s[i+2:]
                    atleast_one_valid = True
                    break
            print(length)
            if atleast_one_valid is False:
                break
        return length

res = Solution().longestValidParentheses("(()())")
print(res)