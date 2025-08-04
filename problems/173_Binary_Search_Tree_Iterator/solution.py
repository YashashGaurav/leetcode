"""
173. Binary Search Tree Iterator
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.go_left(root)

    def go_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        current_node = self.stack.pop()
        self.go_left(current_node.right)
        return current_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
