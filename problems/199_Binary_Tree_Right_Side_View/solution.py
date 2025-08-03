"""
199. Binary Tree Right Side View
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 100% | 60.43%
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = {}

        def dfs(node, level):
            if node == None:
                return

            dfs(node.left, level + 1)
            res[level] = node.val
            dfs(node.right, level + 1)

        dfs(root, 0)

        res = dict(sorted(res.items()))

        return list(res.values())
