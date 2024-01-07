class Solution:
    def plusOne(self, digits):
        index = 1
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
        else:
            if len(digits) > 1:
                digits[-1] = digits[-1] + 1
                while digits[-(index)] == 10 and digits[0] != 10:
                    digits[-index] = 0
                    digits[-(index+1)] = digits[-(index+1)] + 1
                    index += 1
                if digits[0] == 10:
                    digits[0] = 1
                    digits.append(0)
            elif len(digits) == 1:
                digits[-1] = 1
                digits.append(0)
        return digits
        

res = Solution()
result = res.plusOne([9,9,9,9,9,9])
print(result)