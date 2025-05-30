"""
1249. Minimum Remove to Make Valid Parentheses
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(("(", i))
            elif s[i] == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((")", i))

        prob_pos = set()
        for b in stack:
            prob_pos.add(b[1])

        res = ""
        for i in range(len(s)):
            if i not in prob_pos:
                res += s[i]

        return res


# Output: "lee(t(c)o)de"
print(Solution().minRemoveToMakeValid(s="lee(t(c)o)de)"))

# Output: "ab(c)d"
print(Solution().minRemoveToMakeValid(s="a)b(c)d"))

# Output: ""
print(Solution().minRemoveToMakeValid(s="))(("))
