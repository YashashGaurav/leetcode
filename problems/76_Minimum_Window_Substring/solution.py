"""
76. Minimum Window Substring
"""

from collections import defaultdict


class Solution:
    # Beats 5.01% | Beats 54.57%
    def minWindow(self, s: str, t: str) -> str:
        cache = {}
        result_substring = ""

        for character in t:
            if character in cache:
                cache[character][0] += 1
            else:
                cache[character] = [1, 0]

        if len(s) < len(t):
            return ""
        else:
            for idx in range(len(t)):
                if s[idx] in cache:
                    cache[s[idx]][1] -= 1

        left_ptr, right_ptr = 0, len(t) - 1

        while right_ptr < len(s) and left_ptr <= right_ptr:
            if max([sum(_) for _ in cache.values()]) <= 0:
                if (len(result_substring) == 0) or ((right_ptr - left_ptr + 1) < len(result_substring)):
                    result_substring = s[left_ptr : right_ptr + 1]

                if s[left_ptr] in cache:
                    cache[s[left_ptr]][1] += 1

                left_ptr += 1
            else:
                right_ptr += 1

                if right_ptr < len(s) and s[right_ptr] in cache:
                    cache[s[right_ptr]][1] -= 1

        return result_substring


# Output: "BANC"
print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Output: "a"
print(Solution().minWindow(s="a", t="a"))
# Explanation: The entire string s is the minimum window.

# Output: ""
print(Solution().minWindow(s="a", t="aa"))
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.


print(Solution().minWindow(s="bba", t="ab"))

# {'char': [m, -m], 'char2': [n, -n]}

#       r
#     l
# s = stringishere

# t = str

# minWindowLen = len(t)
