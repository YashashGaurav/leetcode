"""
65. Valid Number
"""


class Solution:
    # 100% | 20.42%
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        seen_dot, seen_e, seen_digit = False, False, False

        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in ["e", "E"]:
                if not seen_digit or seen_e:
                    return False
                seen_e = True
                seen_digit = False
            elif char in ["+", "-"]:
                if i > 0 and s[i - 1] not in ["e", "E"]:
                    return False
            elif char == ".":
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            else:
                return False

        return seen_digit
