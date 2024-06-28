"""
question link: https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1
"""

class Solution:
    def armstrongNumber (self, n):
        # code here
        original_num = n
        sum_ = 0
        
        while n > 0:
            last_digit = n % 10
            sum_ += last_digit**3
            n = n//10
        
        return "true" if sum_ == original_num else "false"
    
# Time complexity: O(log(n))
# Space complexity: O(1)
    
sol = Solution()
print(sol.armstrongNumber(153))
print(sol.armstrongNumber(370))