"""
74. Search a 2D Matrix
"""

from typing import List


class Solution:
    # 100% | 72%
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search_ver(top, bottom, target):
            if top > bottom:
                return bottom

            mid = (top + bottom) // 2

            if target > matrix[mid][-1]:
                return binary_search_ver(mid + 1, bottom, target)
            elif target < matrix[mid][0]:
                return binary_search_ver(top, mid - 1, target)
            else:
                return mid

        def binary_search_hor(hor_index, left, right, target):
            if left > right:
                return False

            mid = (left + right) // 2

            if matrix[hor_index][mid] == target:
                return True
            elif matrix[hor_index][mid] < target:
                return binary_search_hor(hor_index, mid + 1, right, target)
            else:
                return binary_search_hor(hor_index, left, mid - 1, target)

        nearest_v_index = binary_search_ver(0, len(matrix) - 1, target)
        return binary_search_hor(nearest_v_index, 0, len(matrix[nearest_v_index]) - 1, target)


print(Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))
print(Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))
print(Solution().searchMatrix(matrix=[[1]], target=0))
print(Solution().searchMatrix(matrix=[[1]], target=2))
