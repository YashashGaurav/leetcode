"""
217. Contains Duplicate
"""

from typing import List


# 7ms, 81.45%
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = set()
        for num in nums:
            if num in cache:
                return True
            else:
                cache.add(num)
        return False


solution = Solution()

nums = [1, 2, 3, 1]
print(solution.containsDuplicate(nums))

nums = [1, 2, 3, 4]
print(solution.containsDuplicate(nums))

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(solution.containsDuplicate(nums))
