from typing import List

class Solution:
    def recurse(self, day, last_index, arr, dp):
        if day == 0:
            points = float('-inf')
            for i in range(3):
                if i != last_index:
                    points = max(points, arr[0][i])
            return points
        
        if dp[day][last_index]:
            return dp[day][last_index]

        max_points = float('-inf')
        for i in range(3):
            if i != last_index:
                max_points = max(max_points, arr[day][i] + self.recurse(day-1, i, arr, dp))
                dp[day][last_index] = max_points
        
        return dp[day][last_index]

    def ninjaTrainingMemoization(self, n: int, points: List[List[int]]) -> int:
        dp = [[None]*4 for _ in range(n)]
        res = self.recurse(n-1, 3, points, dp)
        return res
    
    def ninja_training_tabulation(self, n, points):
        dp = [[None]*4 for _ in range(n)]

        #base cases set for tabulation
        dp[0][0] = max(points[0][1], points[0][2])
        dp[0][1] = max(points[0][0], points[0][2])
        dp[0][2] = max(points[0][0], points[0][1])
        dp[0][3] = max(points[0][1], points[0][2], points[0][0])
        
        #core logic
        for day in range(1, n):
            for last_index in range(4):
                dp[day][last_index] = 0
                for task in range(3):
                    if task != last_index:
                        dp[day][last_index] = max(dp[day][last_index], points[day][task] + dp[day-1][task])
        
        return dp[n-1][3]
    
    def ninja_training_space_optimized(self, n, points):
        prev = [None for _ in range(4)]
    
        prev[0] = max(points[0][1], points[0][2])
        prev[1] = max(points[0][0], points[0][2])
        prev[2] = max(points[0][0], points[0][1])
        prev[3] = max(points[0][1], points[0][2], points[0][0])
        
        #core logic
        for day in range(1, n):
            temp = [None for _ in range(4)]
            for last_index in range(4):
                temp[last_index] = 0
                for task in range(3):
                    if task != last_index:
                        temp[last_index] = max(temp[last_index], points[day][task] + prev[task])
            prev = temp
        
        return prev[3]
    

