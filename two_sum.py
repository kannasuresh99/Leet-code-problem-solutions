#my solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(0,len(nums)):
            first_value = nums[i]
            second_value = target - first_value
            if second_value in set(nums):
                second_value_index = nums.index(second_value)
                if second_value_index != i:
                    res.append(i)
                    res.append(second_value_index)
                    break
        return res

res = Solution()
result = res.twoSum([2,1,9,4,4,56,90,3],8)
print(result)