#my solution
from turtle import st


class Solution:
    def isValid(self, s):
        stack = []
        closeToOpen = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in closeToOpen:
                if stack != [] and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if stack == [] else False

res = Solution()
#result = res.isValid('(){[(]}')
result = res.isValid("(([]){})")
print(result)