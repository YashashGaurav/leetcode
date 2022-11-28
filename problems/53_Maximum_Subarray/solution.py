"""
    53. Maximum Subarray
"""

from typing import List


class Solution:

    # brute force - O(n**3)
    def maxSubArray0(self, nums: List[int]) -> int:

        max_sum = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                max_sum = max(sum(nums[i : j + 1]), max_sum)

        return max_sum

    # O(n**2)
    def maxSubArray1(self, nums: List[int]) -> int:

        max_sum = -10001
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum = nums[i]
            max_sum = max(max_sum, curr_sum)
            for j in range(i + 1, len(nums)):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)

        return max_sum

    # kadane's algo - I'll never remember this - O(n)
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = nums[0]

        for num in nums:
            # reset if the sub array so far has negative
            # total influence
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += num
            max_sum = max(curr_sum, max_sum)

        return max_sum


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
