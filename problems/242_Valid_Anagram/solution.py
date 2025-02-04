"""
242. Valid Anagram
"""


# Feb 04, 2025 00:36
class Solution:
    # 11ms 73.90%
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_counter = [0] * 26

        for i in range(len(s)):
            char_counter[ord(s[i]) - ord("a")] += 1
            char_counter[ord(t[i]) - ord("a")] -= 1

        for i in range(len(char_counter)):
            if char_counter[i] != 0:
                return False

        return True

    # 11ms 73.90%
    def isAnagram_0(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for s_char in s:
            if s_char in s_dict:
                s_dict[s_char] += 1
            else:
                s_dict[s_char] = 1

        for t_char in t:
            if t_char in t_dict:
                t_dict[t_char] += 1
            else:
                t_dict[t_char] = 1

        return s_dict == t_dict


sol = Solution()

s, t = "anagram", "nagaram"
print(sol.isAnagram(s, t))

s, t = "rat", "car"
print(sol.isAnagram(s, t))
