#my solution
class Solution:

    def get_min_len_string(self,string_list):
        min_string_length = None
        for string in string_list:
            if min_string_length != None and min_string_length > len(string):
                min_string_length = len(string)
            elif min_string_length != None and min_string_length < len(string):
                min_string_length = min_string_length
            else:
                min_string_length = len(string)
        return min_string_length

    def longestCommonPrefix(self, strs):
        prefix = ""
        final_prefix = ""
        string_index = 0
        if len(strs) == 1:
            return strs[0]
        minimum_string_length = self.get_min_len_string(strs)
        while string_index < minimum_string_length:
            for i in range(0,len(strs)-1):
                if strs[i][string_index] == strs[i+1][string_index]:
                    prefix = strs[i][string_index]
                else:
                    prefix = ""
                    break
            if prefix != "":
                final_prefix += prefix
            else:
                return final_prefix
            string_index += 1
        return final_prefix

res = Solution()
result = res.longestCommonPrefix(["flower","flow","flowt"])
print(result)