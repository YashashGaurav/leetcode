import numpy as np


class Solution:
    def longestPalindrome(self, input_string: str) -> str:

        string_length = len(input_string)
        dp_store = np.zeros((string_length, string_length), dtype=int)

        max_palindrome: str = input_string[string_length - 1]
        for start in range(string_length - 1, -1, -1):
            for end in range(start, string_length, 1):
                if input_string[start] == input_string[end]:
                    if (
                        end == start
                        or end - start == 1
                        or dp_store[start + 1][end - 1] == 1
                    ):
                        dp_store[start][end] = 1
                        if len(max_palindrome) < end - start + 1:
                            max_palindrome = input_string[start : end + 1]

        return max_palindrome


print(Solution().longestPalindrome("bb"))  # bb
print(Solution().longestPalindrome("babad"))  # bab
print(Solution().longestPalindrome("cbbd"))  # bb
print(Solution().longestPalindrome("a"))  # a
print(Solution().longestPalindrome("ac"))  # a
print(Solution().longestPalindrome("abcdcbabab"))  # abcdcba
print(Solution().longestPalindrome("aacabdkacaa"))  # aca
print(
    Solution().longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
)  # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
