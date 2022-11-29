'''
    124. Binary Tree Maximum Path Sum
'''


import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Accepted	220 ms	21.3 MB
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum = -math.inf
        
        def dfs(node):
            
            if node == None:
                return 0
            
            # maxing here takes care of all possiblities of children being negative
            # freaking GENIUS
            left_sum = max(dfs(node.left), 0) 
            right_sum = max(dfs(node.right), 0) 
            
            # total if we split from here:
            self.max_sum = max(left_sum + right_sum + node.val, self.max_sum)
            
            return max(left_sum, right_sum) + node.val
        
        dfs(root)
        
        return 0 if (self.max_sum == -math.inf) else self.max_sum
