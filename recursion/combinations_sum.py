class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        def combSum(index, candidates, target, subseq_arr):
            if index == len(candidates):
                if target == 0:
                    result.append(subseq_arr[:])
                return

            if candidates[index] <= target:
                subseq_arr.append(candidates[index])
                combSum(index, candidates, target-candidates[index], subseq_arr)
                subseq_arr.pop()
            combSum(index+1, candidates, target, subseq_arr)
            return
        combSum(0, candidates, target, [])
        return result


res = Solution().combinationSum([2,3,6,7,4], 10)
print(res)