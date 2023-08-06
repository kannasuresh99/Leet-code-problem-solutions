from typing import List

#memoization solution
class Solution:
    def recurse(self, stones, curr_pos, k, dp):
        if curr_pos == stones[-1]:
            return True

        if curr_pos not in stones:
            return False

        if (curr_pos, k) in dp:
            return dp[(curr_pos, k)] 
        
        for pos in [k-1, k, k+1]:
            if pos > 0 and self.recurse(stones, curr_pos+pos, pos, dp):
                dp[(curr_pos, k)] = True
                return True
        
        dp[(curr_pos, k)] = False
        return False

    def canCross(self, stones: List[int]) -> bool:
        dp = dict()
        return self.recurse(stones, 0, 0, dp)

#tabulation solution
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        possible_jumps = {stone: set() for stone in stones}
        possible_jumps[0].add(0)

        for i in range(n):
            for jump in possible_jumps[stones[i]]:
                for next_jump in [jump-1, jump, jump+1]:
                    if next_jump > 0 and next_jump+stones[i] in possible_jumps:
                        possible_jumps[next_jump+stones[i]].add(next_jump)

        return len(possible_jumps[stones[-1]]) > 0


