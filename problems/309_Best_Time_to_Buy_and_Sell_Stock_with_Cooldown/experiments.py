"""
309. Best Time to Buy and Sell Stock with Cooldown
"""

from typing import List


class Solution:
    # 50.64% | 38.27%
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(pos, is_buyable):
            if (pos, is_buyable) in cache:
                return cache[(pos, is_buyable)]

            if pos >= len(prices):
                return 0

            if is_buyable:
                res = max(-prices[pos] + dfs(pos + 1, False), dfs(pos + 1, True))

            else:
                res = max(prices[pos] + dfs(pos + 2, True), dfs(pos + 1, False))

            cache[(pos, is_buyable)] = res
            return res

        return dfs(0, True)


# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
print(Solution().maxProfit([1, 2, 3, 0, 2]))

# Output: 0
print(Solution().maxProfit([1]))
