"""
    121. Best Time to Buy and Sell Stock
"""
from typing import List


class Solution:
    # this turned out to be faster
    def maxProfit0(self, prices: List[int]) -> int:
        low = 0
        high = 0
        max_profit = 0

        for s in range(len(prices)):
            if prices[low] > prices[s]:
                low = high = s
            if prices[high] < prices[s]:
                high = s
            if max_profit < (prices[high] - prices[low]):
                max_profit = prices[high] - prices[low]

        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        lowest = 10001
        profit = 0

        for price in prices:
            lowest = min(price, lowest)
            profit = max(profit, price - lowest)

        return profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4, 0, 10]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit([2, 4, 1]))
