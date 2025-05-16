"""
102. Binary Tree Level Order Traversal
"""

from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 100% | 39.42%
    def levelOrder_0(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)

        def dfs(node, level):
            if node is None:
                return

            res[level].append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return list(res.values())

    # 100% | 17.57%
    def levelOrder(self, root: [Optional[TreeNode]]) -> List[List[int]]:
        res = []
        queue = []

        if root is None:
            return res
        else:
            queue.append(root)

        while len(queue) > 0:
            len_queue = len(queue)
            res.append([])

            for _ in range(len_queue):
                node = queue.pop(0)
                res[-1].append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return res


print(Solution().levelOrder(None))
