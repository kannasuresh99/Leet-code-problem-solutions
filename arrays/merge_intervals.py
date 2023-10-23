"""question link: https://leetcode.com/problems/merge-intervals/"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        merged_intervals = []

        intervals.sort(key = lambda x: x[0])

        prev_interval = intervals[0]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev_interval[1]:
                prev_interval[1] = max(prev_interval[1], intervals[i][1])
            else:
                merged_intervals.append(prev_interval)
                prev_interval = intervals[i]
        merged_intervals.append(prev_interval)
        return merged_intervals

