"""
104. Maximum Depth of Binary Tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 37.20% | 7.70%
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if node is None:
                return depth
            else:
                return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))

        return dfs(root, 0)
