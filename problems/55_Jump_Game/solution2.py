"""
55. Jump Game
"""

from typing import List


class Solution:
    # 97.70% | 82.27%
    def canJump(self, nums: List[int]) -> bool:  # shifting the goal back
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0

    # 6.87% | 5.11%
    def canJump_0(self, nums: List[int]) -> bool:
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            if i == len(nums) - 1:
                return True

            if i >= len(nums):
                return False

            if nums[i] == 0:
                return False

            for j in range(nums[i], 0, -1):
                if dfs(i + j):
                    cache[i] = True
                    return cache[i]

            cache[i] = False
            return cache[i]

        return dfs(0)


# Output: true
print(Solution().canJump(nums=[2, 3, 1, 1, 4]))

# Output: false
print(Solution().canJump(nums=[3, 2, 1, 0, 4]))
