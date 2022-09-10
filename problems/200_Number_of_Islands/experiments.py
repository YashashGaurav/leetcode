"""
    200. Number of Islands
"""

from typing import List


class Solution:
    """Accepted	1222 ms	16.5 MB	python3"""
    
    def numIslands(self, grid: List[List[str]]) -> int:

        island_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.grid_dfs(grid, i, j)
                    island_count += 1

        return island_count

    def grid_dfs(self, grid, i, j):
        if (
            i < 0
            or j < 0
            or i > (len(grid) - 1)
            or j > (len(grid[0]) - 1)
            or grid[i][j] != "1"
        ):
            return

        grid[i][j] = "$"
        self.grid_dfs(grid, i - 1, j)
        self.grid_dfs(grid, i + 1, j)
        self.grid_dfs(grid, i, j - 1)
        self.grid_dfs(grid, i, j + 1)


def test_solution():
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(Solution().numIslands(grid))

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(Solution().numIslands(grid))


test_solution()
