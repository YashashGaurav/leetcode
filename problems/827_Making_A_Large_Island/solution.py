"""
827. Making A Large Island
"""

from collections import defaultdict
from typing import List


class Solution:
    # 89.00% | 56.68%
    def largestIsland(self, grid: List[List[int]]) -> int:
        island_dict = defaultdict(lambda: 0)  # id, area
        ROWS = len(grid)
        COLS = len(grid[0])

        # explore the islands
        directions = [
            [-1, 0],
            [0, 1],
            [1, 0],
            [0, -1],
        ]
        id_counter = 1

        def explore_island(island_id, i, j):
            if not (0 <= i < ROWS) or not (0 <= j < COLS):
                return

            if grid[i][j] != 1:
                return

            grid[i][j] = island_id
            island_dict[island_id] += 1

            for direction in directions:
                explore_island(island_id, i + direction[0], j + direction[1])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    id_counter += 1
                    explore_island(id_counter, i, j)

        if id_counter == 1:
            return 1
        elif island_dict[2] == COLS * ROWS:
            return COLS * ROWS

        # flip the water
        max_island_size = 0

        def island_checker(i, j):
            if not (0 <= i < ROWS) or not (0 <= j < COLS):
                return None
            elif grid[i][j] > 1:
                return grid[i][j]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    unique_adj_islands = set()

                    for direction in directions:
                        island_id = island_checker(i + direction[0], j + direction[1])
                        if island_id is not None:
                            unique_adj_islands.add(island_id)

                    neighbor_size = 0
                    for unique_island_id in unique_adj_islands:
                        neighbor_size += island_dict[unique_island_id]

                    max_island_size = max(max_island_size, neighbor_size + 1)

        return max_island_size


# Psuedo:
# calculate area of all the existing islands and mark them
# if all of map is island - n*n is answer
# if none is land - return 1

# flip all 0s to 1 and see adjacent - if island then add that to max possible and return max possible


# Output: 3
print(Solution().largestIsland(grid=[[1, 0], [0, 1]]))

# Output: 4
print(Solution().largestIsland(grid=[[1, 1], [1, 0]]))

# Output: 4
print(Solution().largestIsland(grid=[[1, 1], [1, 1]]))
