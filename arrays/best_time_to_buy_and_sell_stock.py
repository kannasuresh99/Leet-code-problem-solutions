"""
question link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_sell_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            curr_profit = prices[i] - min_sell_price
            max_profit = max(max_profit, curr_profit)
            min_sell_price = min(min_sell_price, prices[i])
        
        return max_profit

