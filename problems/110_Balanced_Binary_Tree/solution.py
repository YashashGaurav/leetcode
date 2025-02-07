'''
    110. Balanced Binary Tree
'''
from typing import List, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 3ms 68.67%
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def _isSubtreeBalanced(node: TreeNode) -> Tuple[bool, int]:
            
            if node is None:
                return True, 0

            # left check
            if node.left is not None:
                is_left_balanced, left_height = _isSubtreeBalanced(node.left)
            else:
                is_left_balanced, left_height = True, -1
            
            # right check
            if node.right is not None:
                is_right_balanced, right_height = _isSubtreeBalanced(node.right)
            else:
                is_right_balanced, right_height = True, -1

            # self balanced check
            if abs(right_height - left_height) <= 1 and is_left_balanced and is_right_balanced:
                is_node_balanced = True
            else:
                is_node_balanced = False
            # self height
            node_height = 1 + max(right_height, left_height)
            
            return is_node_balanced, node_height

        return _isSubtreeBalanced(root)[0]


