"""
70. Climbing Stairs
"""


class Solution:
    # 0ms 17.75mb
    def climbStairs(self, n: int) -> int:
        self.unique_climbs_cache = {}
        return self.recurse_back(n)

    def recurse_back(self, n):
        if n in self.unique_climbs_cache:
            return self.unique_climbs_cache[n]

        if n <= 0:
            return n == 0
        else:
            ways = self.recurse_back(n - 1) + self.recurse_back(n - 2)
            self.unique_climbs_cache[n] = ways
            return ways


# time out issues.
class Solution0:
    def climbStairs(self, n: int) -> int:
        self.unique_climbs = 0
        self.recurse_back(n)
        return self.unique_climbs

    def recurse_back(self, n):
        if n < 0:
            return
        elif n == 0:
            self.unique_climbs += 1
        elif n > 0:
            self.recurse_back(n - 1)
            self.recurse_back(n - 2)


# Output: 2
print(Solution().climbStairs(n=2))

# Output: 3
print(Solution().climbStairs(n=3))


print(Solution().climbStairs(n=38))
