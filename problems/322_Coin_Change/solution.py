"""
322. Coin Change
"""

from typing import List


class Solution:
    # 18.60% | 10.58%
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(amount):
            if amount == 0:
                return 0

            if amount in cache:
                return cache[amount]

            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            cache[amount] = res
            return res

        min_coins = dfs(amount)
        if min_coins >= 1e9:
            return -1
        else:
            return min_coins

    # Greedy - didn't work
    def coinChange_0(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins, reverse=True)
        res = 0

        def find_max(coin, amt):
            return int(amt / coin), (amt % coin)

        for coin in coins:
            if amount > 0:
                temp_c, amount = find_max(coin, amount)
                res += temp_c

        if amount == 0:
            return res
        else:
            return -1


print(Solution().coinChange(coins=[1, 2, 5], amount=11))

print(Solution().coinChange(coins=[2], amount=3))

print(Solution().coinChange(coins=[1], amount=0))

print(Solution().coinChange(coins=[186, 419, 83, 408], amount=6249))
