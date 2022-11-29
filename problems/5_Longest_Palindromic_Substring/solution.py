import numpy as np


class Solution:
    # Accepted	3524 ms	14.4 MB
    def longestPalindrome0(self, input_string: str) -> str:

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
                            max_palindrome = input_string[start: end + 1]

        return max_palindrome

    # neetcode style checking
    # Accepted	1347 ms	13.9 MB
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        
        for i in range(len(s)):
            l, r = i, i
            while l > -1 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l: r+1]
                l -= 1
                r += 1
                
        for i in range(len(s)):
            l, r = i, i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l: r+1]
                l -= 1
                r += 1
            
        return res


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
