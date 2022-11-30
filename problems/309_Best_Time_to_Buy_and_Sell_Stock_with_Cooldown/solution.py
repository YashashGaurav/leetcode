'''
    309. Best Time to Buy and Sell Stock with Cooldown
'''

class Solution:
    # Accepted	103 ms	17.8 MB
    def maxProfit(self, prices: List[int]) -> int:

        self.max_time = len(prices)        
        dp = {}

        def dfs(time_p, isBought):
            
            if time_p >= self.max_time:
                return 0
            
            if (time_p, isBought) in dp:
                return dp[(time_p, isBought)]
            
            if not isBought: # can buy
                profit = max(
                    dfs(time_p + 1, not isBought) - prices[time_p], # buying
                    dfs(time_p + 1, isBought) # cooldown
                )
            if isBought: # can sell
                profit = max(
                    dfs(time_p + 2, not isBought) + prices[time_p], # selling
                    dfs(time_p + 1, isBought), # cooldown
                )
            
            dp[(time_p, isBought)] = profit
            return dp[(time_p, isBought)]
        
        return dfs(0, False)