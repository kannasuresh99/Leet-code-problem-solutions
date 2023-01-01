class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        def CombSum(idx, arr, subseq_arr, target):
            if idx == len(arr):
                if target == 0:
                    result.append(subseq_arr[:])
                return

            if arr[idx] <= target:
                #pickup
                subseq_arr.append(arr[idx])
                CombSum(idx, arr, subseq_arr, target-arr[idx])
                subseq_arr.pop()

            #don't pickup
            CombSum(idx+1, arr, subseq_arr, target)
            return
        CombSum(0, candidates, [], target)
        return result


res = Solution().combinationSum([2,3,6,7,4], 10)
print(res)