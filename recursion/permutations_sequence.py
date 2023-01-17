import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k = k - 1
        nums = [i for i in range(1, n+1)]
        ans = ""

        while len(nums) > 0:
            dividend = math.factorial(len(nums))//len(nums)
            index = k//dividend
            ans += str(nums[index])
            k %= dividend
            nums.remove(nums[index])

        return ans
        
res = Solution().getPermutation(4, 17)
print(res)