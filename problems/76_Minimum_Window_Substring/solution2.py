"""
76. Minimum Window Substring
"""

from collections import defaultdict


class Solution:
    # 14.03% | 93.31%

    def minWindow(self, s: str, t: str) -> str:
        char_map = defaultdict(lambda: [0, 0])

        for char in t:
            char_map[char][0] += 1

        l, r = 0, 0

        def is_char_map_full():
            for char, val in char_map.items():
                if val[0] > val[1]:
                    return False

            return True

        res = ""

        while r < len(s):
            if s[r] in char_map:
                char_map[s[r]][1] += 1

            while is_char_map_full() and l <= r:
                if len(res) == 0 or len(res) > r - l:
                    res = s[l : r + 1]

                # decrement
                if s[l] in char_map:
                    char_map[s[l]][1] -= 1

                l += 1

            r += 1

        return res


# l, r = 0, 0
# char_map[c] = [actuals, present]

# while r < len(s):

#     if s[r] in char_map:
#         char_map[s[r]][1] += 1

#     while sufficiency_checker:
#         if len(res) > r - l:
#             res = s[l: r+1]

#         # decrement
#         char_map[s[l]][1] -= 1
#         l += 1

#     r += 1


print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))

print(Solution().minWindow(s="a", t="a"))

print(Solution().minWindow(s="a", t="aa"))
