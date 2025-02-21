"""
136. Single Number
"""

from typing import List


class Solution:
    # 0ms | Mem 77.74%
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result ^ num

        return result

    # 5ms - 39.79% | Mem 7.69%
    def singleNumber0(self, nums: List[int]) -> int:
        cache = set()
        for i in nums:
            if i not in cache:
                cache.add(i)
            elif i in cache:
                cache.remove(i)

        return next(iter(cache))


print(Solution().singleNumber(nums=[2, 2, 1]))
print(Solution().singleNumber(nums=[4, 1, 2, 1, 2]))
print(Solution().singleNumber(nums=[1]))
