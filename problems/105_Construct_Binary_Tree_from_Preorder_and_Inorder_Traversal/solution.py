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
    # Accepted	388 ms	53.5 MB
    def buildTree0(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:

        self.preorder = preorder

        def dfs(inorder):

            if not inorder:
                return None

            curr_val = self.preorder.pop(0)
            node = TreeNode(curr_val)

            in_split_index = inorder.index(curr_val)

            left_inorder_list = inorder[:in_split_index].copy()
            right_inorder_list = inorder[in_split_index + 1 :].copy()

            node.left = dfs(left_inorder_list)
            node.right = dfs(right_inorder_list)
            return node

        return dfs(inorder)

    # neetcode figured out that we can use the length of the of the first
    # n numbers till the mid node will belong to the left subtree and
    # post mid will belong to the right subtree - even in the preorder list
    # GENIUS
    # Accepted	193 ms	88.7 MB
    def buildTree(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        node = TreeNode(preorder[0])
        inorder_mid = inorder.index(preorder[0])
        node.left = self.buildTree(
            preorder[1 : inorder_mid + 1], inorder[:inorder_mid]
        )
        node.right = self.buildTree(
            preorder[inorder_mid + 1 :], inorder[inorder_mid + 1 :]
        )
        return node


# self.preorder = [20,15,7]

# dfs([9,3,15,20,7])
# curr_val = 3
# in_split_index = 1
# inorder = [9,3,15,20,7]
# left_inorder_list = [9]
# right_inorder_list = [15, 20, 7]

# dfs([9])
# curr_val = 9
# in_split_index = 0
# inorder = [9]
# left_inorder_list = []
# right_inorder_list = []

# dfs([15, 20, 7])
# curr_val = 20
# in_split_index = 1
# inorder = [15, 20, 7]
# left_inorder_list = [15]
# right_inorder_list = [7]
