"""
314. Binary Tree Vertical Order Traversal
"""

from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: TreeNode) -> list[list[int]]:
        collector = defaultdict(list)

        def dfs(node, x, y):
            if not node:
                return

            collector[y].append([x, node.val])

            if node.left:
                dfs(node.left, x + 1, y - 1)
            if node.right:
                dfs(node.right, x + 1, y + 1)

        dfs(root, 0, 0)

        min_col, max_col = min(list(collector.keys())), max(list(collector.keys()))

        output = []
        for icol in range(min_col, max_col + 1):
            col_output = collector[icol].sort(lambda key: key[0])

            output.append([val[0] for val in col_output])

        return output

    def verticalOrder(self, root: TreeNode) -> list[list[int]]:
        q = deque()

        q.append((root, 0, 0))
        # visited.add()
        res = defaultdict(list)

        while q:
            for _ in range(len(q)):
                node, row, col = q.popleft()

                res[col].append((node.val, row))

                if node.left:
                    q.append((node.left, row + 1, col - 1))
                if node.right:
                    q.append((node.right, row + 1, col + 1))

        min_col, max_col = min(list(res.keys())), max(list(res.keys()))

        output = []
        for icol in range(min_col, max_col + 1):
            col_output = res[icol].sort(lambda key: key[1])

            output.append([val[0] for val in col_output])

        return output
