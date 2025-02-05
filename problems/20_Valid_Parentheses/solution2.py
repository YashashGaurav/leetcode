"""
20. Valid Parentheses
"""


class Solution:
    # 15ms 4.21% - Feb 05, 2025 01:00
    def isValid(self, s: str) -> bool:
        match_dict = {"{": "}", "(": ")", "[": "]"}
        stack = []

        for char in s:
            stack.append(char)

            if len(stack) > 1 and match_dict.get(stack[-2]) == stack[-1]:
                stack = stack[:-2]

        return len(stack) == 0


sol = Solution()

print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([])"))
