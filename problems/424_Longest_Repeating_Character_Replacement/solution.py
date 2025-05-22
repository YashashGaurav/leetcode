"""
424. Longest Repeating Character Replacement
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int):
        # neetcode solution

        cache = {}
        max_freq = 0
        left = 0
        max_len = 0

        for right in range(len(s)):
            cache[s[right]] = 1 + cache.get(s[right], 0)
            max_freq = max(max_freq, cache[s[right]])

            while (right - left + 1) - max_freq > k:
                cache[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

    # 5%
    def characterReplacement_1(self, s: str, k: int) -> int:
        def check(cache):
            cache_list = sorted(cache.items(), key=lambda item: item[1], reverse=True)
            return sum([v for k, v in cache_list[1:]]) <= k

        max_size = 0
        left, right = 0, 0
        cache = defaultdict(lambda: 0)

        while left < len(s) and right < len(s):
            cache[s[right]] += 1
            if check(cache):
                max_size = max(max_size, sum(cache.values()))
            else:
                while not check(cache):
                    cache[s[left]] -= 1
                    left += 1
            right += 1

        return max_size

    # bruteforce O(n2) - TLE
    def characterReplacement_0(self, s: str, k: int) -> int:
        max_size = 0

        def check(cache):
            cache_list = sorted(cache.items(), key=lambda item: item[1], reverse=True)
            return sum([v for k, v in cache_list[1:]]) <= k

        for left in range(0, len(s)):
            right = left
            cache = defaultdict(lambda: 0)
            while right < len(s):
                cache[s[right]] += 1

                if check(cache):
                    max_size = max(max_size, sum(cache.values()))
                else:
                    break
                right += 1

        return max_size


# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
print(Solution().characterReplacement(s="ABAB", k=2))

# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
print(Solution().characterReplacement(s="AABABBA", k=1))


print(Solution().characterReplacement(s="KAAKAAA", k=2))
