"""
235. Lowest Common Ancestor of a Binary Search Tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 60 ms | Beats 48.56%
class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        def dfs(node):
            if p.val > node.val and q.val > node.val:
                return dfs(node.right)
            elif p.val < node.val and q.val < node.val:
                return dfs(node.left)
            else:
                return node

        return dfs(root)
