class Solution:
    def get_sub_arr(self,num):
        divisor = 10
        sub_num_array = []
        temp = num
        if num%divisor == 0:
            num = num//10
        while num%divisor == 0:
            num = num // 10
        multiply_factor = temp//num
        while num%divisor != 0:
            sub_num = num%divisor
            sub_num_array.insert(0,sub_num)
            num -= sub_num
            divisor *= 10
        if num != 0:
            sub_num_array.insert(0,num)
        for i in range(0,len(sub_num_array)):
            sub_num_array[i] *= multiply_factor
        return sub_num_array
    def intToRoman(self, num: int) -> str:
        roman_num = ""
        sub_num_array = []
        divisor = 10
        temp = num
        new_arr = []
        roman_dict = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        one_to_ten_dict = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X'}
        ten_to_hundred_dict = {10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC',100:'C'}
        hundred_to_thousand_dict = {100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM',1000:'M'}
        thousand_to_threethousand_dict = {1000:'M',2000:'MM',3000:'MMM'}
        if num <= 10:
            return one_to_ten_dict[num]
        if num in roman_dict:
            return roman_dict[num]
        if num%10 == 0:
            sub_num_array = self.get_sub_arr(num)
        else:
            while num%divisor != 0:
                if divisor > num:
                    break
                sub_num = num%divisor
                sub_num_array.insert(0,sub_num)
                num -= sub_num
                if num%10 == 0:
                    if num in [10,50,100,500,1000]:
                        break
                    new_arr = self.get_sub_arr(num)
                    break
                divisor *= 10
                if divisor > 1000:
                    divisor = 1000
            if num != 0 and new_arr == []:
                sub_num_array.insert(0,num)
            if new_arr:
                for n in sub_num_array:
                    new_arr.append(n)
                sub_num_array = new_arr
        for val in sub_num_array:
            if val >= 1000:
                roman_num += thousand_to_threethousand_dict[val]
            elif val >= 100:
                roman_num += hundred_to_thousand_dict[val]
            elif val >= 10:
                roman_num += ten_to_hundred_dict[val]
            elif val < 10:
                roman_num += one_to_ten_dict[val]
        return roman_num


res = Solution()
result = res.intToRoman(158)
print(result)