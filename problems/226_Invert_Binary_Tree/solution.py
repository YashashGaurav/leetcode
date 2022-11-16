"""
    226. Invert Binary Tree
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Should have implemented this but could make it work
# without this ¯\_(ツ)_/¯
# class Tree:
#     def __init__(self):
#         self.root = None

#     def add_node(val):
#         if not root:
#             root = TreeNode()


#     def create_tree(self, arr):
#         add_node()

# Accepted	62 ms	13.8 MB
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            return self._invert(root)

    def _invert(self, node: TreeNode):
        if node.left:
            node.left = self._invert(node.left)
        if node.right:
            node.right = self._invert(node.right)

        temp = node.left
        node.left = node.right
        node.right = temp
        return node


# print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
# print(Solution().search([-1, 0, 3, 5, 9, 12], 2))
# print(Solution().search([5], 5))
