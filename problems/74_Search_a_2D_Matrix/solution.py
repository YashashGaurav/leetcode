"""
    74. Search a 2D Matrix
"""
from typing import List


class Solution:
    def searchMatrix0(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        width = len(matrix[0])
        height = len(matrix)
        end = (width * height) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if matrix[mid // width][mid % width] < target:
                start = mid + 1
            elif matrix[mid // width][mid % width] > target:
                end = mid - 1
            else:
                return True
        return False

    # faster but heavier
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width, height = len(matrix[0]), len(matrix)

        # search in among rows:
        top, bottom = 0, height - 1
        while top <= bottom:
            row = top + (bottom - top) // 2
            if matrix[row][0] > target:
                bottom = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break

        if top > bottom:
            return False

        left, right = 0, width - 1
        row = top + (bottom - top) // 2
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                return True
        return False


print(
    Solution().searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
    )
)
print(
    Solution().searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13
    )
)
print(Solution().searchMatrix(matrix=[[1, 3]], target=3))

