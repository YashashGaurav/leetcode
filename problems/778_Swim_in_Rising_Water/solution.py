"""
778. Swim in Rising Water
"""

import heapq
from typing import List


class Solution:
    # 83% | 52%
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = COLS = len(grid)
        minHeap = [(grid[0][0], 0, 0)]  # (max(curr, next), r, c)
        visited = set([(0, 0)])
        directions = [
            [-1, 0],
            [0, 1],
            [1, 0],
            [0, -1],
        ]

        while minHeap:
            curr_h, curr_r, curr_c = heapq.heappop(minHeap)

            if curr_r == ROWS - 1 and curr_c == COLS - 1:
                return curr_h

            for direction in directions:
                next_r = direction[0] + curr_r
                next_c = direction[1] + curr_c

                if (0 <= next_r < ROWS) and (0 <= next_c < ROWS) and (next_r, next_c) not in visited:
                    visited.add((next_r, next_c))
                    heapq.heappush(minHeap, (max(curr_h, grid[next_r][next_c]), next_r, next_c))


# Output: 3
print(Solution().swimInWater(grid=[[0, 2], [1, 3]]))

# Output: 16
print(
    Solution().swimInWater(
        grid=[[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    )
)
