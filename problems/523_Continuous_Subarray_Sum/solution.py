"""
523. Continuous Subarray Sum
"""

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0: -1}
        pre_fix_sum = 0

        for index, num in enumerate(nums):
            pre_fix_sum += num
            pre_fix_rem = pre_fix_sum % k

            if pre_fix_rem not in remainders:
                remainders[pre_fix_rem] = index
            elif abs(remainders[pre_fix_rem] - index) > 1:
                return True

        return False


# true
print(Solution().checkSubarraySum(nums=[23, 2, 4, 6, 7], k=6))

# true
print(Solution().checkSubarraySum(nums=[23, 2, 6, 4, 7], k=6))

# false
print(Solution().checkSubarraySum(nums=[23, 2, 6, 4, 7], k=13))
