'''
    100. Same Tree
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # Accepted runtime: 99.53% and Memory 98.71%
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p, q):

            if p == None and q == None:
                return True

            if ((p == None and q != None) or 
                (q == None and p != None) or 
                (p.val != q.val)):
                return False
            
            if dfs(p.left, q.left) and dfs(p.right, q.right):
                return True

        
        return dfs(p, q)

            

# p = [1, 2, 3]
# q = [1, 2, 3]

# dfs(1, 1)
# dfs(2, 2)
# dfs(None, None)