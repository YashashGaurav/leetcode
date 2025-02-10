"""
572. Subtree of Another Tree
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 43 ms Beats 60.85% - Feb 09, 2025 23:11
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def _sub_tree_check(node, subRoot):
            if (node is None and subRoot is not None) or (node is not None and subRoot is None):
                return False
            if node is None and subRoot is None:
                return True

            if node.val == subRoot.val:
                return _sub_tree_check(node.left, subRoot.left) and _sub_tree_check(node.right, subRoot.right)

            return False

        def dfs(node, subRoot):
            if subRoot is None:
                return True
            if node is None:
                return False

            if _sub_tree_check(node, subRoot):
                return True
            else:
                return dfs(node.left, subRoot) or dfs(node.right, subRoot)

        return dfs(root, subRoot)
