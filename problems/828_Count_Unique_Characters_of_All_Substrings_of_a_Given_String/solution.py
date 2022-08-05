"""
    828. Count Unique Characters of All Substrings of a Given String
"""


class Solution0:
    def unique_letters_in(self, s: str) -> int:
        unique_store = set()
        dup_store = set()
        for char in s:
            if char in unique_store:
                dup_store.add(char)
            else:
                unique_store.add(char)
        return len(unique_store) - len(dup_store)

    def uniqueLetterString(self, s: str) -> int:
        uniqueCount = 0
        for i in range(1, len(s) + 1):
            for j in range(len(s) - i + 1):
                uniqueCount += self.unique_letters_in(s[j : i + j])
        return uniqueCount


class Solution1:  # Accepted	606 ms	18.7 MB
    def uniqueLetterString(self, s: str) -> int:
        indexes = {}
        for idx, char in enumerate(s):
            if char in indexes:
                indexes[char].append(idx)
            else:
                indexes[char] = [idx]

        unique_sum = 0
        for key in indexes:
            for i in range(len(indexes[key])):
                right_unique_substrings = 0
                left_unique_substrings = 0
                # calculate left_unique_substrings
                if i == 0:
                    left_unique_substrings = indexes[key][i] + 1
                else:
                    left_unique_substrings = (
                        indexes[key][i] - indexes[key][i - 1]
                    )
                # calculate right_unique_substrings
                if i == len(indexes[key]) - 1:
                    right_unique_substrings = len(s) - indexes[key][i]
                else:
                    right_unique_substrings = (
                        indexes[key][i + 1] - indexes[key][i]
                    )
                unique_sum += right_unique_substrings * left_unique_substrings

        return unique_sum


class Solution:  # Accepted	7277 ms	14.8 MB
    def uniqueLetterString(self, s: str) -> int:

        left = 0
        right = 0
        ret_sum = 0

        for i in range(len(s)):
            j = i - 1
            while j >= 0:
                if s[i] == s[j]:
                    break
                j -= 1
            left = i - j

            j = i + 1
            while j < len(s):
                if s[i] == s[j]:
                    break
                j += 1
            right = j - i

            ret_sum += right * left

        return ret_sum


print(Solution().uniqueLetterString("ABC"))
print(Solution().uniqueLetterString("ABA"))
print(Solution().uniqueLetterString("LEETCODE"))
