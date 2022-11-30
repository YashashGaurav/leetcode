"""
    230. Kth Smallest Element in a BST
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Accepted	103 ms	18.1 MB
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative inorder traversal
        stack = [root]
        curr = root
        visited = set()

        while True:

            if curr:
                stack.append(curr)
                curr = curr.left

            elif stack:
                curr = stack.pop()
                k -= 1
                if k == 0:
                    return curr.val

                curr = curr.right

            else:
                break

        return False

    # 	Accepted	58 ms	18.2 MB
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # do in order and get kth pop

        self.stack = []
        self.k = k

        def dfs(node):

            if not node:
                return -1

            self.stack.append(node)

            # left first
            res = dfs(node.left)
            if res != -1:
                return res

            # self second
            self.k -= 1
            if self.k == 0:
                return self.stack.pop().val
            else:
                self.stack.pop()

            # right last
            res = dfs(node.right)
            if res != -1:
                return res

            return -1

        return dfs(root)


# stack = [3, 2, 1]
# curr = node(1)
# k = 2
