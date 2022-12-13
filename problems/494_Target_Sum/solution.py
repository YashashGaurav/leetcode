'''
    494. Target Sum
'''

from typing import List

class Solution:

    # Accepted 865ms 35.9mb
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        arr_len = len(nums)
        dp = {}

        def dfs(idx, total):
            if idx == arr_len: 
                if target == total:
                    return 1 
                return 0
            
            if (idx, total) in dp:
                return dp[(idx, total)]

            dp[(idx, total)] = (
                dfs(idx + 1, total + nums[idx]) + 
                dfs(idx + 1, total - nums[idx])
            )

            return dp[(idx, total)]
        
        return dfs(0, 0)



# [1, 1, 1, 1, 1], target = 3
# dfs(0, 0)
# neg_total = -1
# neg_total = +1

# dfs(1, -1)
# neg_total = -2
# neg_total = 0

# dfs(1, 1)
# neg_total = -2
# neg_total = 0