"""
    198. House Robber
"""

from typing import List


class Solution:
    
    # Accepted	69 ms	13.8 MB
    def rob0(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)

        max_rob = max(nums[-2:])

        for i in range(len(nums) - 3, -1, -1):
            nums[i] += max(nums[i + 2 :])
            max_rob = max(max_rob, nums[i])

        return max_rob

    # Accepted	46 ms	13.9 MB	
    # neetcode style - accumulation of results
    def rob(self, nums: List[int]) -> int:
        
        rob_1, rob_2 = 0, 0
        
        for i in range(len(nums) - 1, -1, -1):
            temp = max(nums[i] + rob_2, rob_1)
            rob_2 = rob_1
            rob_1 = temp
        
        return rob_1


print(Solution().rob([2, 7, 9, 3, 1]))  # 12
print(Solution().rob([2, 1, 1, 2]))  # 4

