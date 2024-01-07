
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i] >= goal:
                goal = i
            print(i,nums[i],goal)
        if goal == 0:
            return True
        return False
            

res = Solution()
result = res.canJump([1,1,1,1,0])
print(result)