#recursive solution
class Solution:
    def recurse(self, idx, target, arr):
        if target == 0:
            return True
        if idx == 0:
            if arr[idx] == target:
                return True
            return False
        
        #pickup scenario
        pick = False
        if target >= arr[idx]:
            pick = self.recurse(idx-1, target-arr[idx], arr)
        
        #not pickup scenario
        not_pick = self.recurse(idx-1, target, arr)
        
        return pick or not_pick
        
        
    def isSubsetSum (self, N, arr, sum):
        # code here
        return self.recurse(N-1, sum, arr)

#memoization solution
class Solution:
    def recurse(self, idx, target, arr, dp):
        if target == 0:
            return True
        if idx == 0:
            if arr[idx] == target:
                return True
            return False
            
        if dp[idx][target]:
            return dp[idx][target]
        
        #pickup scenario
        pick = False
        if target >= arr[idx]:
            pick = self.recurse(idx-1, target-arr[idx], arr, dp)
        
        #not pickup scenario
        not_pick = self.recurse(idx-1, target, arr, dp)
        
        dp[idx][target] = pick or not_pick
        
        return dp[idx][target]
        
        
    def isSubsetSum (self, N, arr, sum):
        # code here
        dp = [[None]*(sum+1) for _ in range(N)]
        return self.recurse(N-1, sum, arr, dp)

#tabulation solution
class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here
        dp = [[False]*(sum+1) for _ in range(N)]
        
        # Setting base cases
        for i in range(N):
            dp[i][0] = True
            
        dp[0][0] = True
        if arr[0] <= sum:
            dp[0][arr[0]] = True
        
        # Core logic
        for idx in range(1, N):
            for target in range(1, sum+1):
                pick = False
                if target >= arr[idx]:
                    pick = dp[idx-1][target-arr[idx]]
                not_pick = dp[idx-1][target]
        
                dp[idx][target] = pick or not_pick
        return dp[N-1][sum]

