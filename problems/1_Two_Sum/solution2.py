"""
1. Two Sum
"""

from typing import List


class Solution:
    # 1ms | 34.22%
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            if target - nums[i] in cache:
                return [i, cache[target - nums[i]]]
            else:
                cache[nums[i]] = i


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
print(Solution().twoSum(nums=[3, 2, 4], target=6))
print(Solution().twoSum(nums=[3, 3], target=6))
