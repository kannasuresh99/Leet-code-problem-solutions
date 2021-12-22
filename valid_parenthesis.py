#my solution
class Solution:
    def isValid(self, s):
        bracket_dict = {'(':
                            {'open':'(','close':')'},
                        '[':
                            {'open':'[','close':']'},
                        '{':
                            {'open':'{','close':'}'}
                        }
        result = True
        while result == True:
            s = list(s)
            if len(s) % 2 != 0:
                return False
            if s:
                for i in range(0,len(s)):
                    if s[i] not in bracket_dict:
                        return False
                    else:
                        if bracket_dict[s[i]]['close'] not in s:
                            return False
                        if i != len(s)-1:
                            if s[i+1] == bracket_dict[s[i]]['close']:
                                result = True
                                if len(s) > 2:
                                    del s[i]
                                    del s[i]
                                    break
                                elif len(s) == 2:
                                    return result
                            else:
                                result = False
                        else:
                            return result
            else:
                return result
        return result

res = Solution()
result = res.isValid('(){[(]}')
#result = res.isValid("(([]){})")
print(result)