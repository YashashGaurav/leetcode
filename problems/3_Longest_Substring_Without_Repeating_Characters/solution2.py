"""
3. Longest Substring Without Repeating Characters
"""


class Solution:
    # 57.12% | 82.26%
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        cache = set()
        ileft, iright = 0, 0

        while iright < len(s):
            if s[iright] not in cache:
                cache.add(s[iright])
                res = max(res, iright - ileft + 1)
                iright += 1
            else:
                cache.remove(s[ileft])
                ileft += 1

        return res


print(Solution().lengthOfLongestSubstring(s="abcabcbb"))
print(Solution().lengthOfLongestSubstring(s="bbbbb"))
print(Solution().lengthOfLongestSubstring(s="pwwkew"))
print(Solution().lengthOfLongestSubstring(s="aab"))
print(Solution().lengthOfLongestSubstring(s="dvdf"))
