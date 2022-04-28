"""
    20. Valid Parentheses
"""


class Solution:
    def isValid0(self, s: str) -> bool:
        pairs = [["{", "}"], ["[", "]"], ["(", ")"]]
        stack = []

        for c in s:
            stack.append(c)
            if stack[-2:] in pairs:
                stack = stack[:-2]

        return stack == []

    # faster than above
    def isValid(self, s: str) -> bool:
        # using a dict rather than array.
        pairs = {"{": "}", "[": "]", "(": ")"}
        stack = []

        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if len(stack) > 0 and pairs[stack[-1]] == c:
                    stack = stack[:-1]
                else:
                    return False

        return stack == []


print(Solution().isValid("()"))  # true
print(Solution().isValid("()[]{}"))  # true
print(Solution().isValid("(]"))  # false
print(Solution().isValid("[[{[{()}]}]]"))  # true
print(Solution().isValid("]"))  # False
