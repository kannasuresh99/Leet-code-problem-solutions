#my solution
class Solution:
    def romanToInt(self, s):
        result = 0
        roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sub_score_list = []
        ignore_index = []
        score = 0
        for index in range(0,len(s)):
            if index != len(s)-1:
                if roman_dict[s[index]] >= roman_dict[s[index+1]] and index not in set(ignore_index):
                    result = roman_dict[s[index]]
                    sub_score_list.append(result)
                if roman_dict[s[index]] < roman_dict[s[index+1]] and index not in set(ignore_index):
                    result = roman_dict[s[index+1]] - roman_dict[s[index]]
                    sub_score_list.append(result)
                    ignore_index.append(index+1)
            else:
                if roman_dict[s[index]] <= roman_dict[s[index-1]] and index not in set(ignore_index):
                    result = roman_dict[s[index]]
                    sub_score_list.append(result)
        for sub_score in sub_score_list:
            score += sub_score
        return score

res = Solution()
result = res.romanToInt("MCMXCVI")
print(result)