#my solution
class Solution:
    def romanToInt(self, s):
        result = 0
        roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        curr_max = float('-inf')
        for i in range(len(s)-1,-1,-1):
            if roman_dict[s[i]] >= curr_max:
                curr_max = roman_dict[s[i]]
                result += roman_dict[s[i]]
            else:
                result -= roman_dict[s[i]]
            print(curr_max,result)
        return result

res = Solution()
result = res.romanToInt("MCMXCVI")
print(result)