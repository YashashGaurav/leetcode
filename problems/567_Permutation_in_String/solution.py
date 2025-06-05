"""
567. Permutation in String
"""


class Solution:
    # Beats 25.29% | Beats 98.03%
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)

        def char_map(s):
            s_char_map = [0 for _ in range(26)]

            for c in s:
                s_char_map[ord(c) - ord("a")] += 1

            return s_char_map

        s1_char_map = char_map(s1)
        s2_char_map = char_map(s2[: len(s1)])

        matches = sum([1 if s1_char_map[i] == s2_char_map[i] else 0 for i in range(len(s1_char_map))])

        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True

            s2_char_map[ord(s2[i - s1_len]) - ord("a")] -= 1
            s2_char_map[ord(s2[i]) - ord("a")] += 1

            # can do better here.
            matches = sum([1 if s1_char_map[i] == s2_char_map[i] else 0 for i in range(len(s1_char_map))])

        return matches == 26

    # TLE
    def checkInclusion_0(self, s1: str, s2: str) -> bool:
        def permute(s):
            if len(s) == 0:
                return [[]]

            sub_perms = permute(s[1:])
            perms = []

            for sub_perm in sub_perms:
                for i in range(len(sub_perm) + 1):
                    sub_perm_copy = sub_perm.copy()
                    sub_perm_copy.insert(i, s[0])
                    perms.append(sub_perm_copy)

            return perms

        permutations = permute(s1)

        for permutation in permutations:
            temp = "".join(permutation)
            if temp in s2:
                return True

        return False


# Output: true
print(Solution().checkInclusion(s1="ab", s2="eidbaooo"))

# Output: false
print(Solution().checkInclusion(s1="ab", s2="eidboaoo"))
