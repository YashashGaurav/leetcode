"""
1. Two Sum
"""

from typing import List


class Solution:
    # 0ms, 100.0%
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            if target - nums[i] in store:
                return [store[target - nums[i]], i]
            else:
                store[nums[i]] = i

    # 1785ms 18.61%
    def twoSum_0(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
print(Solution().twoSum(nums=[3, 2, 4], target=6))
print(Solution().twoSum([3, 3], target=6))
