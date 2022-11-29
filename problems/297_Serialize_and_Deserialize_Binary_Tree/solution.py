"""
    297. Serialize and Deserialize Binary Tree
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    # Accepted	309 ms	20.5 MB
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        stack = [root]
        res = []

        while stack:
            curr = stack.pop()
            if curr == None:
                res.append("N")
                continue

            res.append(str(curr.val))

            stack.append(curr.right)
            stack.append(curr.left)

        print(",".join(res))
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        tree_list = data.split(",")
        self.curr_index = 0

        def dfs():

            if tree_list[self.curr_index] == "N":
                self.curr_index += 1
                return None

            node = TreeNode(tree_list[self.curr_index])
            self.curr_index += 1

            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


#
# stack = 5,None
#
# 1,2,N,N,3,4,N,N,5,N,N
#
#
#
#
#
#
#
#
#
#
#
#
