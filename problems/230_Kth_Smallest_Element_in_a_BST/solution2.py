"""
230. Kth Smallest Element in a BST
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 100.00% | 27.00%
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        parent_stack = []
        curr = root
        n = 0

        while curr or parent_stack:
            while curr:
                parent_stack.append(curr)
                curr = curr.left

            curr = parent_stack.pop()
            n += 1
            if n == k:
                return curr.val

            curr = curr.right

    def kthSmallest_0(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def in_order(node):
            if node is None:
                return
            if len(res) == k:
                return

            if node.left:
                in_order(node.left)

            res.append(node.val)

            if node.right:
                in_order(node.right)

        in_order(root)
        return res[k - 1]
