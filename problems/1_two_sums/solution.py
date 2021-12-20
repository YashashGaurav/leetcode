from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref_table = {}
        for i, num1 in enumerate(nums):
            if target - num1 in ref_table:
                return [ref_table[target - num1], i]
            else:
                ref_table[num1] = i
        return [0, 0]


solution = Solution()
print(solution.twoSum([3, 2, 4], 6))
