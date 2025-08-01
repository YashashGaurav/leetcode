"""
987. Vertical Order Traversal of a Binary Tree
"""

from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 100% | 60%
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_dict = defaultdict(lambda: defaultdict(lambda: []))

        def dfs(node, row, col):
            if node == None:
                return

            if col_dict[col][row]:
                col_dict[col][row] = sorted(col_dict[col][row] + [node.val])
            else:
                col_dict[col][row].append(node.val)

            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        col_dict = dict(sorted(col_dict.items()))

        res = []
        for row_dict in col_dict.values():
            row_dict = dict(sorted(row_dict.items()))
            row_res = []
            for row in row_dict.values():
                row_res = row_res + row

            res.append(row_res)

        return res
