"""
518. Coin Change II
"""

from typing import List


class Solution:
    # 29.99% | 21.70%
    def change(self, amount: int, coins: List[int]) -> int:
        coins = sorted(coins, reverse=True)
        cache = {}

        def dfs(amount, coin_ptr):
            if amount == 0:
                return 1
            if coin_ptr >= len(coins):
                return 0
            if (amount, coin_ptr) in cache:
                return cache[(amount, coin_ptr)]

            res = dfs(amount, coin_ptr + 1)
            if amount - coins[coin_ptr] >= 0:
                res += dfs(amount - coins[coin_ptr], coin_ptr)
            cache[(amount, coin_ptr)] = res
            return res

        return dfs(amount, 0)


print(Solution().change(amount=4, coins=[1, 2, 3]))
print(Solution().change(amount=7, coins=[2, 4]))
print(Solution().change(amount=100, coins=[99, 1]))
print(Solution().change(amount=500, coins=[1, 2, 5]))
