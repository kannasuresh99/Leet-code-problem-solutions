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
            limiting_string = b
            string_starting_index = len(a) - len(b)
            sum_prefix = a[:string_starting_index]
            a = a[string_starting_index:]
        elif len(b) > len(a):
            limiting_string = a
            string_starting_index = len(b) - len(a)
            sum_prefix = b[:string_starting_index]
            b = b[string_starting_index:]
        elif len(a) == len(b):
            limiting_string = a
            sum_prefix = None
        for i in range(len(limiting_string)-1,-1,-1): 
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

        if sum_prefix:
            if carry_on:
                result = result [1:]
                while carry_on:
                    if len(sum_prefix) == 1:
                        sum_ = self.getBinarySum(sum_prefix[-1],carry_on)
                        result = sum_ + result
                        return result
                    else:
                        sum_ = self.getBinarySum(sum_prefix[-1],carry_on)
                        if sum_ == '10':
                            sum_ = '0'
                            result = sum_ + result
                            carry_on = '1'
                            sum_prefix = sum_prefix[:-1]
                        else:
                            result = sum_ + result
                            sum_prefix = sum_prefix[:-1]
                            result = sum_prefix + result
                            carry_on = None
            else:
                result = sum_prefix + result
        return result