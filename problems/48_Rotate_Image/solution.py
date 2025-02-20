"""
48. Rotate Image
"""

from typing import List


class Solution:
    # 0ms - Mem - Beats 41.96%
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # transpose
        for i in range(ROWS):
            for j in range(i + 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # H-flip
        for i in range(ROWS):
            for j in range(COLS // 2):
                matrix[i][j], matrix[i][COLS - 1 - j] = matrix[i][COLS - 1 - j], matrix[i][j]

        return matrix


# Output: [[7,4,1],[8,5,2],[9,6,3]]
print(Solution().rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
print(Solution().rotate(matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
