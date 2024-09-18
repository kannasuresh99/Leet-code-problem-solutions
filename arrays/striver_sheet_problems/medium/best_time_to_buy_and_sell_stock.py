"""
Problem: Best Time to Buy and Sell Stock
Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buying_cost = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            curr_profit = prices[i] - min_buying_cost
            max_profit = max(max_profit, curr_profit)
            min_buying_cost = min(min_buying_cost, prices[i])
        
        return max_profit

res = Solution().maxProfit([7,1,5,3,6,4])
print(res)
