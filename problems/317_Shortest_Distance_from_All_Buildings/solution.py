"""
317. Shortest Distance from All Buildings
"""

from collections import deque


class Solution:
    def shortestDistance(self, grid: list[list[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        # dis, i-thBuildings
        distance_stores = [[(0, 0) for _ in range(COLS)] for _ in range(ROWS)]
        total_buildings = 0
        valid_directions = [
            [-1, 0],  # top
            [0, 1],  # right
            [1, 0],  # bottom
            [0, -1],  # left
        ]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    total_buildings += 1

                    layer_deque = deque([[row, col, 0]])
                    visited_set = set()
                    visited_set.add((0, 0))

                    while layer_deque:
                        curr_row, curr_col, dist = layer_deque.popleft()
                        distance_stores[curr_row][curr_col] = (
                            distance_stores[curr_row][curr_col][0] + dist,
                            distance_stores[curr_row][curr_col][1] + 1,
                        )

                        for dir_row, dir_col in valid_directions:
                            row_next, col_next = curr_row + dir_row, curr_col + dir_col

                            if (
                                (0 <= row_next < ROWS)
                                and (0 <= col_next < COLS)
                                and ((row_next, col_next) not in visited_set)
                                and (grid[row_next][col_next] == 0)
                            ):
                                layer_deque.append([row_next, col_next, dist + 1])
                                visited_set.add((row_next, col_next))

        min_distance = 1e9
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0 and distance_stores[row][col][1] == total_buildings:
                    min_distance = min(min_distance, distance_stores[row][col][0])

        return min_distance if min_distance != 1e9 else -1

    def shortestDistance_0(self, grid: list[list[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        distance_stores = [[(0, 0) for _ in range(COLS)] for _ in range(ROWS)]
        visited_set = set()
        total_buildings = 0
        valid_directions = [
            [-1, 0],  # top
            [0, 1],  # right
            [1, 0],  # bottom
            [0, -1],  # left
        ]

        def store_distance(row, col, dist):
            if (row, col) in visited_set:
                return

            visited_set.add((row, col))
            distance_stores[row][col] = (distance_stores[row][col][0] + dist, distance_stores[row][col][1] + 1)

            for direction in valid_directions:
                row_new = row + direction[0]
                col_new = col + direction[1]

                if (
                    (row_new < ROWS)
                    and (row_new >= 0)
                    and (col_new < COLS)
                    and (col_new >= 0)
                    and ((row_new, col_new) not in visited_set)
                    and (grid[row_new][col_new] not in (1, 2))
                ):
                    layer_deque.append([row_new, col_new, dist + 1])

            while layer_deque:
                store_distance(*layer_deque.popleft())

            # add neighbors if not in visited_set or not a 1 or 2 or out of bounds

            # for traverse with store_distance(dist+1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    visited_set = set()
                    layer_deque = deque()
                    total_buildings += 1
                    store_distance(row, col, 0)

        min_distance = 1e9
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0 and distance_stores[row][col][1] == total_buildings:
                    min_distance = min(min_distance, distance_stores[row][col][0])

        return min_distance if min_distance != 1e9 else -1


# Output: 7
print(Solution().shortestDistance(grid=[[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))

# Output: 1
print(Solution().shortestDistance(grid=[[1, 0]]))

# # Output: -1
print(Solution().shortestDistance(grid=[[1]]))
