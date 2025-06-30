"""
162. Find Peak Element
"""

from typing import List


class Solution:
    # 100% | 60.99%
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float("-inf")] + nums + [float("-inf")]
        left = 1
        right = len(nums) - 2

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid - 1

            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif nums[mid] < nums[mid - 1]:
                right = mid - 1

        return left - 1
