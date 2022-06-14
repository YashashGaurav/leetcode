"""
    704. Binary Search
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)

    def binary_search0(
        self, nums: List[int], start: int, end: int, target: int
    ) -> int:

        mid = start + ((end - start) // 2)  # better for the overflow problem

        if nums[mid] == target:
            return mid
        elif end - start == 0:
            return -1
        elif nums[mid] < target:
            return self.binary_search(nums, mid + 1, end, target)
        else:
            return self.binary_search(nums, start, mid, target)

    def binary_search(
        self, nums: List[int], start: int, end: int, target: int
    ) -> int:

        mid = start + ((end - start) // 2)

        if start > end:
            return -1
        elif nums[mid] > target:
            return self.binary_search(nums, start, mid - 1, target)
        elif nums[mid] < target:
            return self.binary_search(nums, mid + 1, end, target)
        else:
            return mid


print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
print(Solution().search([-1, 0, 3, 5, 9, 12], 2))
print(Solution().search([5], 5))
