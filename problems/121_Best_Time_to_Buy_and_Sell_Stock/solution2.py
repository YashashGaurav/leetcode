"""
121. Best Time to Buy and Sell Stock
"""

from typing import List


class Solution:
    # 125ms 31.70% - Feb 05, 2025 00:09
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy_price = prices[0]

        for sell_price in prices:
            max_profit = max(max_profit, sell_price - min_buy_price)
            min_buy_price = min(min_buy_price, sell_price)

        return max_profit

    # 155ms 6.41%
    def maxProfit_1(self, prices: List[int]) -> int:
        min_ptr, max_ptr, max_profit = 0, 0, 0

        while max_ptr < len(prices) - 1:
            if prices[min_ptr] < prices[max_ptr + 1]:
                max_ptr += 1
            elif prices[min_ptr] >= prices[max_ptr + 1]:
                max_ptr += 1
                min_ptr = max_ptr

            max_profit = max(max_profit, prices[max_ptr] - prices[min_ptr])

        return max(0, max_profit)

    # TLE
    def maxProfit_0(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                max_profit = max(max_profit, prices[j] - prices[i])

        return max(0, max_profit)


sol = Solution()

print(sol.maxProfit([7, 1, 5, 3, 6, 4]))

print(sol.maxProfit([7, 6, 4, 3, 1]))
