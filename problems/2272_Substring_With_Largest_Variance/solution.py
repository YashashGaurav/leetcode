"""
    2272. Substring With Largest Variance
"""

import itertools


# Time Limit Exceeded
class Solution0:
    def largestVariance(self, s: str) -> int:
        largest_var = 0

        for i in range(0, len(s)):
            count_dict = {s[i]: 1}
            for j in range(i + 1, len(s)):
                if s[j] in count_dict:
                    count_dict[s[j]] += 1
                else:
                    count_dict[s[j]] = 1

                if len(count_dict) > 1:
                    char_freq = sorted(count_dict.values(), reverse=True)
                    if largest_var < (char_freq[0] - char_freq[-1]):
                        largest_var = char_freq[0] - char_freq[-1]

        return largest_var


# Ref: https://leetcode.com/problems/substring-with-largest-variance/discuss/2038774
# Kadane's algo: https://www.youtube.com/watch?v=5WZl3MMT0Eg&t=190s
# Time Limit Exceeded
class Solution1:
    def largestVariance(self, s: str) -> int:
        chars = set(s)
        ret_var = 0
        for a, b in itertools.permutations(chars, 2):
            if a == b:  # Same chars so ignore them
                continue
            char_high_freq = char_low_freq = 0
            # abandoned_low_freq to be turned true
            # if char_low_freq > char_high_freq
            # and we still have have chars in string s to go through.
            # helps dealing with not having to reverse string as mentioned
            # here:
            # https://youtu.be/DbfHIdZL8rQ?t=956
            abandoned_low_freq = False
            for c in s:
                if a == c:
                    char_high_freq += 1
                elif b == c:
                    char_low_freq += 1
                if char_low_freq > char_high_freq:
                    # resetting as per Kadane's
                    char_high_freq = 0
                    char_low_freq = 0
                    abandoned_low_freq = True
                    continue

                if char_low_freq > 0:
                    ret_var = max(ret_var, char_high_freq - char_low_freq)
                elif abandoned_low_freq:
                    ret_var = max(ret_var, char_high_freq - 1)

        return ret_var


# did not use max() - Passed.
# Accepted	6118 ms	13.8 MB
class Solution:
    def largestVariance(self, s: str) -> int:
        chars = set(s)
        ret_var = 0
        for a, b in itertools.permutations(chars, 2):
            if a == b:  # Same chars so ignore them
                continue
            char_high_freq = char_low_freq = 0
            abandoned_low_freq = False
            for c in s:

                if a == c:
                    char_high_freq += 1
                elif b == c:
                    char_low_freq += 1

                # resetting as per Kadane's
                if char_low_freq > char_high_freq:
                    char_high_freq = 0
                    char_low_freq = 0
                    abandoned_low_freq = True
                    continue

                if char_low_freq > 0:
                    if ret_var < (char_high_freq - char_low_freq):
                        ret_var = char_high_freq - char_low_freq
                elif abandoned_low_freq:
                    if ret_var < (char_high_freq - 1):
                        ret_var = char_high_freq - 1

        return ret_var


print(Solution().largestVariance("aababbb"))  # 3
print(Solution().largestVariance("aabbbbaa"))  # 3
print(Solution().largestVariance("abcde"))  # 0
print(Solution().largestVariance("icexiahccknibwuwgi"))  # 3
