class Solution:
    #using eucledian algorithm
    def gcd_of_numbers(self,num1,num2):
        if num1 < num2:
            temp = num1
            num1 = num2
            num2 = temp
        if num2 == 0:
            return num1
        else:
            remainder = num1%num2
            return self.gcd_of_numbers(num2,remainder)

res = Solution()
result = res.gcd_of_numbers(25,250)
print(result)
