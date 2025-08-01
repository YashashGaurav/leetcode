"""
301. Remove Invalid Parentheses
"""

from collections import deque
from typing import List


class Solution:
    # 71.93% | 36.81%
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(input):
            stack = []

            for char in input:
                if char == ")":
                    if len(stack) > 0:
                        stack.pop()
                    else:
                        return False
                elif char == "(":
                    stack.append(char)

            if len(stack) > 0:
                return False
            else:
                return True

        bfs_queue = deque([s])
        best_level_found = False
        visited = set([s])
        res = set()

        while bfs_queue:
            level_len = len(bfs_queue)
            for i in range(level_len):
                process_string = bfs_queue.popleft()
                if is_valid(process_string):
                    res.add(process_string)
                    best_level_found = True
                elif not best_level_found:
                    for i in range(len(process_string)):
                        if process_string[i] in ["(", ")"]:
                            child_test_string = process_string[:i] + process_string[i + 1 :]
                            if child_test_string not in visited:
                                visited.add(child_test_string)
                                bfs_queue.append(child_test_string)

        return list(res)


# Output: ["(())()","()()()"]
print(Solution().removeInvalidParentheses(s="()())()"))


# Output: ["(a())()","(a)()()"]
print(Solution().removeInvalidParentheses(s="(a)())()"))


# Output: [""]
print(Solution().removeInvalidParentheses(s=")("))


print(Solution().removeInvalidParentheses(s="((((((((((((((((((aaaaa))"))
