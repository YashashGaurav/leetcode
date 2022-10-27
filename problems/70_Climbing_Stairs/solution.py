"""
    70. Climbing Stairs
"""

# Accepted	61 ms	13.9 MB
class Solution:

    def __init__(self):
        self.step_store = {}

    def _count_steps(self, n: int):
        if n < 2:
            return 1
        if n not in self.step_store:
            left = self._count_steps(n - 1)
            right = self._count_steps(n - 2)
            self.step_store[n] = left + right
        return self.step_store[n]

    def climbStairs(self, n: int) -> int:
        return self._count_steps(n)



print(Solution().climbStairs(16))
print(Solution().climbStairs(5))
print(Solution().climbStairs(1))
print(Solution().climbStairs(45))
