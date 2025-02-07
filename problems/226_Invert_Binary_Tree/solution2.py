'''
    226. Invert Binary Tree
'''

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 0ms, 100%
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def reverse_node(node: TreeNode):

            if node is None:
                return None
            
            if node.left is not None:
                node.left = reverse_node(node.left)
            if node.right is not None:
                node.right = reverse_node(node.right)
            
            node.right, node.left = node.left, node.right

            return node
        
        return reverse_node(root)