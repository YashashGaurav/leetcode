from math import floor


class Solution:
    def longestPalindrome(self, s: str) -> str:

        char_dict = {}
        for index, char in enumerate(s):
            if char in char_dict:
                char_dict[char] += [index]
            else:
                char_dict[char] = [index]

        def is_palindrome(string: str, start: int, end: int) -> bool:
            check_counts = floor((end - start + 1) / 2) - 1
            check_index = start + 1
            while check_counts > 0:
                if string[check_index] != string[end - (check_index - start)]:
                    return False
                check_counts -= 1
                check_index += 1
            return True

        max_palindrome: str = ""
        for char in char_dict:
            for i in range(len(char_dict[char])):
                j = len(char_dict[char]) - 1
                while j >= i:
                    if is_palindrome(
                        s, char_dict[char][i], char_dict[char][j]
                    ) and len(max_palindrome) < (
                        char_dict[char][j] - char_dict[char][i] + 1
                    ):
                        max_palindrome = s[char_dict[char][i]: char_dict[char][j] + 1]
                        break
                    j -= 1

        return max_palindrome


# print(Solution().longestPalindrome("babad"))  # bab
# print(Solution().longestPalindrome("cbbd"))  # bb
# print(Solution().longestPalindrome("a"))  # a
# print(Solution().longestPalindrome("ac"))  # a
# print(Solution().longestPalindrome("abcdcbabab"))  # abcdcba
# print(Solution().longestPalindrome("aacabdkacaa"))  # aca
print(Solution().longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))  # aca
