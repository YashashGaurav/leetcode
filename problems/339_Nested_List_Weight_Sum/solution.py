"""
339. Nested List Weight Sum
"""

from typing import List

# class NestedInteger:
#     def __init__(self, value=None):
#         """
#         If value is not specified, initializes an empty list.
#         Otherwise initializes a single integer equal to value.
#         """

#     def isInteger(self):
#         """
#         @return True if this NestedInteger holds a single integer, rather than a nested list.
#         :rtype bool
#         """

#     def add(self, elem):
#         """
#         Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#         :rtype void
#         """

#     def setInteger(self, value):
#         """
#         Set this NestedInteger to hold a single integer equal to value.
#         :rtype void
#         """

#     def getInteger(self):
#         """
#         @return the single integer that this NestedInteger holds, if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         :rtype int
#         """

#     def getList(self):
#         """
#         @return the nested list that this NestedInteger holds, if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         :rtype List[NestedInteger]
#         """


class Solution:
    # premium question
    def depthSum(self, nestedList: List) -> int:
        return_val_list = []

        def sum_it_up(sublist, depth):
            for num in sublist:
                if type(num) is list:
                    sum_it_up(num, depth + 1)
                else:
                    return_val_list.append(depth * num)

        sum_it_up(nestedList, 1)
        return sum(return_val_list)


# 10
print(Solution().depthSum([[1, 1], 2, [1, 1]]))
# 27
print(Solution().depthSum([1, [4, [6]]]))
