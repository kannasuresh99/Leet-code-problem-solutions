#my solution
class Solution:
    def removeElement(self, nums, val):
        while val in set(nums):
            print(nums)
            for i in range(0,len(nums)):
                if nums[i] == val:
                    del nums[i]
                    break
        return len(nums)

res = Solution()
result = res.removeElement([3,2,2,3],3)
print(result)