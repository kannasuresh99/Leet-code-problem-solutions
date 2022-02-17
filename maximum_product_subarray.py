
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 1:
            return 0
        _max = current_max = current_min = nums[0]
        current_max = 1
        current_min = 1

        for i in range(1,len(nums)):
            if nums[i] == 0:
                current_max = 1
                current_min = 1
                continue
            temp = current_max
            current_max = max(nums[i]*current_max, nums[i]*current_min, nums[i])
            current_min = max(nums[i]*temp, nums[i]*current_min, nums[i])
            _max = max(_max,current_max)
        return _max
             


res = Solution()
#result = res.maxProduct([-2,0,-1])
result = res.maxProduct([-2,3,-4])
print(result)