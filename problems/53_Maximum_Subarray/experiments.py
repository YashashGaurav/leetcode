"""
53. Maximum Subarray
"""

import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dfs(i, j):
            if i > j:
                return -(math.inf)

            m = (i + j) // 2

            left_max_sum, curr_sum, right_max_sum = 0, 0, 0
            for a in range(m, i, -1):
                curr_sum += nums[a]
                left_max_sum = max(curr_sum, left_max_sum)

            curr_sum = 0
            for a in range(m, j):
                curr_sum += nums[a]
                right_max_sum = max(curr_sum, right_max_sum)

            return max(dfs(i, m - 1), left_max_sum + nums[m] + right_max_sum, dfs(m + 1, j))

        return dfs(0, len(nums) - 1)

    # 58ms - 32.90MB
    def maxSubArray1(self, nums: List[int]) -> int:
        # remove previous if it makes sum smaller:
        current_max, result_max = nums[0], nums[0]

        for i in range(1, len(nums)):
            if current_max < 0:
                current_max = 0

            current_max += nums[i]
            result_max = max(result_max, current_max)

        return result_max

    # time out
    def maxSubArray0(self, nums: List[int]) -> int:
        current_max: int = nums[0]

        for i in range(len(nums)):
            sub_array_max = 0
            for j in range(i, len(nums)):
                sub_array_max += nums[j]
                current_max = max(current_max, sub_array_max)
        return current_max


print(Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().maxSubArray(nums=[1]))
print(Solution().maxSubArray(nums=[5, 4, -1, 7, 8]))
print(Solution().maxSubArray(nums=[-2, 1]))
