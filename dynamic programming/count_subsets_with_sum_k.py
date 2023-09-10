#recursive solution
from typing import List

def recurse(idx, target, arr):
    if target == 0:
        return 1
    
    if idx == 0:
        if arr[0] == target:
            return 1
        return 0
    
    #pick
    pick = 0
    if arr[idx] <= target:
        pick = recurse(idx-1, target-arr[idx], arr)
    
    not_pick = recurse(idx-1, target, arr)

    return pick + not_pick

def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    n = len(arr)
    return recurse(n-1, k, arr)

#memoization solution
from typing import List

def recurse(idx, target, arr, dp):
    if target == 0:
        return 1
    
    if idx == 0:
        if arr[0] == target:
            return 1
        return 0
    
    if dp[idx][target]:
        return dp[idx][target]

    #pick
    pick = 0
    if arr[idx] <= target:
        pick = recurse(idx-1, target-arr[idx], arr, dp)
    
    not_pick = recurse(idx-1, target, arr, dp)

    dp[idx][target] = pick + not_pick

    return dp[idx][target]

def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    n = len(arr)
    dp = [[None]*(k+1) for _ in range(n)]
    return recurse(n-1, k, arr, dp)%(10**9 + 7)

#tabulation solution
from typing import List

def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    n = len(arr)
    dp = [[0]*(k+1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    
    if arr[0] <= k:
        dp[0][arr[0]] = 1

    for idx in range(1, n):
        for target in range(k+1):
            pick = 0
            if arr[idx] <= target:
                pick = dp[idx-1][target-arr[idx]]
            
            not_pick = dp[idx-1][target]

            dp[idx][target] = pick + not_pick

    return dp[n-1][k]%(10**9 + 7)

