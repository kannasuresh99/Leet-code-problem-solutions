class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        visited = [False]*len(nums)
        nums.sort()

        def permutationRecursion(nums, perm_arr):
            if len(perm_arr) == len(nums):
                result.append(perm_arr[:])
                return
            
            for i in range(0, len(nums)):
                if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue
                perm_arr.append(nums[i])
                visited[i] = True
                permutationRecursion(nums, perm_arr)
                perm_arr.pop()
                visited[i] = False
            
        permutationRecursion(nums, [])
        return result

res = Solution().permuteUnique([1,1,1])
print(res)