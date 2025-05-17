"""
695. Max Area of Island
"""

from typing import List


class Solution:
    # 47.56 | 17.81%
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited_island_cell = set()
        max_island_size = 0

        def explore_island(irow, jcol):
            nonlocal visited_island_cell
            current_island_size = 0

            def explore_cell(irow, jcol):
                nonlocal current_island_size
                nonlocal visited_island_cell

                if grid[irow][jcol] == 1 and (irow, jcol) not in visited_island_cell:
                    current_island_size += 1
                    visited_island_cell.add((irow, jcol))
                    if irow > 0:  # up
                        explore_cell(irow - 1, jcol)
                    if irow < ROWS - 1:  # down
                        explore_cell(irow + 1, jcol)
                    if jcol > 0:  # left
                        explore_cell(irow, jcol - 1)
                    if jcol < COLS - 1:
                        explore_cell(irow, jcol + 1)

            explore_cell(irow, jcol)
            return current_island_size

        for irow in range(ROWS):
            for jcol in range(COLS):
                if grid[irow][jcol] == 1 and (irow, jcol) not in visited_island_cell:
                    max_island_size = max(explore_island(irow, jcol), max_island_size)

        return max_island_size


# Output: 6
print(
    Solution().maxAreaOfIsland(
        grid=[
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
)

# Output: 0
print(Solution().maxAreaOfIsland(grid=[[0, 0, 0, 0, 0, 0, 0, 0]]))
