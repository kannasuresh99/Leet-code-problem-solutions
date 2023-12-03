"""
question link: https://leetcode.com/problems/string-to-integer-atoi/
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        """
        4230
        10^(4-1)
        4000
        10^(3-1)
        200
        10^(2-1)
        30
        """
        if s == "":
            return 0

        #step1: check for trailing spaces
        left = 0
        right = len(s)-1

        while left < right and (s[left] == " " or s[right] == " "):
            if s[left] == " ":
                left += 1
            if s[right] == " ":
                right -= 1
        
        #step2: check if its negative
        is_integer_negative = False
        if s[left] == '-':
            is_integer_negative = True
            left += 1
        elif s[left] == '+':
            left += 1
        
        #step3: parsing integer string
        integer_dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        integer_str = ""
        while left <= right and s[left] in integer_dict:
            integer_str += s[left]
            left += 1
        
        #step4: calculating integer sum
        n = len(integer_str)
        i = 0
        res = 0
        while i < len(integer_str):
            res += (integer_dict[integer_str[i]]*(10**(n-1)))
            i += 1
            n -= 1
        if is_integer_negative == True:
            res *= -1
        if res > (2**31)-1:
            res = (2**31)-1
        elif res < -(2**31):
            res = -(2**31)
        return res

res = Solution().myAtoi(s="4193 with words")
print(res)
