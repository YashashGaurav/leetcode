"""
150. Evaluate Reverse Polish Notation
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif token == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif token == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif token == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))
            else:
                stack.append(int(token))

        return stack.pop()


# print(Solution().evalRPN(tokens=["1", "2", "+", "3", "*", "4", "-"]))
print(Solution().evalRPN(tokens=["4", "13", "5", "/", "+"]))
