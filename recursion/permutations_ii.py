class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        #nums.sort()

        def Perm2(idx, nums):
            if idx == len(nums):
                result.append(nums)
                return

            for i in range(idx, len(nums)):
                if (i > idx) and (nums[i] == nums[idx]):
                    continue
                if i > idx:
                    nums[i],nums[idx] = nums[idx],nums[i]
                    Perm2(idx+1, nums[:])
                elif i == idx:
                    Perm2(idx+1, nums[:])
            return
        Perm2(0, nums)
        return result

res = Solution().permuteUnique(["foo", "bar", "work"])
print(res)