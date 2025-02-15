"""
62. Unique Paths
"""


class Solution:
    # 0ms - 18.02 MB
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m - 1, n - 1
        cache = {}

        def move(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i > ROWS or j > COLS:
                return 0
            elif i == ROWS and j == COLS:
                return 1

            cache[(i, j)] = move(i + 1, j) + move(i, j + 1)
            return cache[(i, j)]

        return move(0, 0)


print(Solution().uniquePaths(m=3, n=7))
print(Solution().uniquePaths(m=3, n=2))
