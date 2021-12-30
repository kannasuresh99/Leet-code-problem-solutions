#my solution
class Solution:
    def getBinarySum(self,x,y):
        sum = ''
        if x == y:
            if x == '1':
                sum = '10'
            elif x == '0':
                sum = '0'
        elif (x == '0' and y == '1') or (x == '1' and y == '0'):
            sum = '1'
        elif x == '10':
            sum = '11'
        return sum

    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry_on = None
        if len(a) > len(b):
            string_starting_index = len(a) - len(b)
            b = '0'*string_starting_index + b
        elif len(b) > len(a):
            string_starting_index = len(b) - len(a)
            a = '0'*string_starting_index + a

        for i in range(len(a)-1,-1,-1): 
            if carry_on:
                sum_ = self.getBinarySum(a[i],b[i])
                sum_ = self.getBinarySum(sum_,carry_on)
            else:
                sum_ = self.getBinarySum(a[i],b[i])
            #handling carry over addition
            if sum_ == '10':
                if i != 0:
                    sum_ = '0'
                    carry_on = '1'
                else:
                    carry_on = '1'
            elif sum_ == '11':
                if i != 0:
                    sum_ = '1'
                    carry_on = '1'
                else:
                    carry_on = '1'
            else:
                carry_on = None
            result = sum_ + result

        return result

res = Solution()
result = res.addBinary("1111","11")
print(result)