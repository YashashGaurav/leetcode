"""
105. Construct Binary Tree from Preorder and Inorder Traversal
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Beats 15.68% | Beats 11.36%
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root = TreeNode(val=preorder[0])
        pivot = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : pivot + 1], inorder[:pivot])
        root.right = self.buildTree(preorder[1 + pivot :], inorder[pivot + 1 :])

        return root


# Output: [3,9,20,null,null,15,7]
print(Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))

# Output: [-1]
print(Solution().buildTree(preorder=[-1], inorder=[-1]))


# p = [3, 9, 20, 15, 7]

# i = [9, 3, 15, 20, 7]
