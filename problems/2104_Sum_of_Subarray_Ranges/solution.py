"""
    2104. Sum of Subarray Ranges
"""

from typing import List


class Solution0:
    def subArrayRanges(self, nums: List[int]) -> int:

        ret = 0
        for subset_size in range(1, len(nums) + 1):
            for start_index in range(0, len(nums) + 1 - subset_size):
                ret += max(
                    nums[start_index : start_index + subset_size]
                ) - min(nums[start_index : start_index + subset_size])
        return ret


class Solution1:
    """Accepted	7351 ms	14 MB python3"""

    def subArrayRanges(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            _min = _max = nums[i]
            for j in range(i + 1, len(nums)):
                _min = min(_min, nums[j])
                _max = max(_max, nums[j])
                ret += _max - _min

        return ret


# Ref: https://leetcode.com/problems/sum-of-subarray-ranges/discuss/1979763/Python-Stack-O(n)-Solution-with-inline-explanation
# Could not understand, moving on.
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        # the answer will be sum{ Max(subarray) - Min(subarray) } over all
        # possible subarray
        # which decomposes to sum{Max(subarray)} - sum{Min(subarray)} over all
        # possible subarray
        # so totalsum = maxsum - minsum
        # we calculate minsum and maxsum in two different loops
        minsum = maxsum = 0

        # first calculate sum{ Min(subarray) } over all subarrays
        # sum{ Min(subarray) } = sum(f(i) * nums[i]) ; i=0..n-1
        # where f(i) is number of subarrays where nums[i] is the minimum value
        # f(i) = (i - index of the previous smaller value) * (index of the
        # next smaller value - i) * nums[i]
        # we can claculate these indices in linear time using a monotonically
        # increasing stack.
        stack = []
        for next_smaller_idx in range(n + 1):
            # we pop from the stack in order to satisfy the monotonically
            # increasing order property
            # if we reach the end of the iteration and there are elements
            # present in the stack, we pop all of them
            while stack and (
                next_smaller_idx == n
                or nums[stack[-1]] > nums[next_smaller_idx]
            ):
                i = stack.pop()
                prev_smaller_idx = stack[-1] if stack else -1
                minsum += (
                    nums[i] * (next_smaller_idx - i) * (i - prev_smaller_idx)
                )
            stack.append(next_smaller_idx)

        # then calculate sum{ Max(subarray) } over all subarrays
        # sum{ Max(subarray) } = sum(f'(i) * nums[i]) ; i=0..n-1
        # where f'(i) is number of subarrays where nums[i] is the maximum value
        # f'(i) = (i - index of the previous larger value) - (index of the
        # next larger value - i) * nums[i]
        # this time we use a monotonically decreasing stack.
        stack = []
        for next_larger in range(n + 1):
            # we pop from the stack in order to satisfy the monotonically
            # decreasing order property
            # if we reach the end of the iteration and there are elements
            # present in the stack, we pop all of them
            while stack and (
                next_larger == n or nums[stack[-1]] < nums[next_larger]
            ):
                i = stack.pop()
                prev_larger = stack[-1] if stack else -1
                maxsum += nums[i] * (next_larger - i) * (i - prev_larger)
            stack.append(next_larger)

        return maxsum - minsum


print(Solution().subArrayRanges([1, 2, 3]))  # 4
print(Solution().subArrayRanges([1, 3, 3]))  # 4
print(Solution().subArrayRanges([4, -2, -3, 4, 1]))  # 59
