"""
    198. House Robber
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)

        max_rob = max(nums[-2:])

        for i in range(len(nums) - 3, -1, -1):
            nums[i] += max(nums[i + 2 :])
            max_rob = max(max_rob, nums[i])

        return max_rob


print(Solution().rob([2, 7, 9, 3, 1]))  # 12
print(Solution().rob([2, 1, 1, 2]))  # 4

