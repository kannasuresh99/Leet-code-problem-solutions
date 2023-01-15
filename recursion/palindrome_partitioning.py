class Solution:
    def isPalindrome(self, str_):
        left = 0
        right = len(str_)-1

        while left < right:
            if str_[left] != str_[right]:
                return False
            left += 1
            right -= 1

        return True

    def partition(self, s: str):
        result = []

        def PartitionPalindromeString(idx, partition_arr):
            if idx == len(s):
                result.append(partition_arr[:])
                return

            for i in range(idx, len(s)):
                if self.isPalindrome(s[idx:i+1]):
                    partition_arr.append(s[idx:i+1])
                    PartitionPalindromeString(i+1, partition_arr)
                    partition_arr.pop()

            return
        PartitionPalindromeString(0, [])
        return result

res = Solution().partition("aabb")
print(res)
