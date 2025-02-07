"""
704. Binary Search
"""

from typing import List


class Solution:
    # 0ms - 100% - recursive
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right, nums, target):
            mid = int((left + right) / 2)
            # or
            mid = left + (right - left) // 2

            if left > right:
                return -1

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, right, nums, target)
            elif nums[mid] > target:
                return binary_search(left, mid - 1, nums, target)

        return binary_search(0, len(nums) - 1, nums, target)

    # 0ms, 100% - iterative
    def search0(self, nums: List[int], target: int) -> int:
        left_ptr, right_ptr = 0, len(nums) - 1

        while left_ptr <= right_ptr:
            mid_ptr = int((right_ptr + left_ptr) / 2)
            if nums[mid_ptr] == target:
                return mid_ptr
            elif nums[mid_ptr] < target:
                left_ptr = mid_ptr + 1
            elif nums[mid_ptr] > target:
                right_ptr = mid_ptr - 1

        return -1


print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=9))
# left = 0
# right = 5
# mid =

print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=2))

print(Solution().search(nums=[5], target=5))
