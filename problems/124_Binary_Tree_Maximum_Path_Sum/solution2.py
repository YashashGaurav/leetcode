"""
124. Binary Tree Maximum Path Sum
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float("-inf")

        def dfs(node):
            nonlocal max_path_sum

            if node is None:
                return 0

            left_max_path = max(dfs(node.left), 0)
            right_max_path = max(dfs(node.right), 0)

            my_max_path = left_max_path + right_max_path + node.val
            max_path_sum = max(my_max_path, max_path_sum)

            parent_max_path = node.val + max(left_max_path, right_max_path)

            return parent_max_path

        dfs(root)
        return int(max_path_sum)


# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# print(Solution().maxPathSum(root=[1, 2, 3]))


# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
# print(Solution().maxPathSum(root=[-10, 9, 20, null, null, 15, 7]))
