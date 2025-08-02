"""
1216. Valid Palindrome III
"""


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def dfs(left, right, remaining_k):
            nonlocal s

            if left == right and remaining_k >= 0:
                return True

            if s[left] == s[right]:
                return dfs(left + 1, right - 1, remaining_k)
            elif remaining_k > 0:
                return dfs(left + 1, right, remaining_k - 1) or dfs(left, right - 1, remaining_k - 1)
            else:
                return False

        return dfs(0, len(s) - 1, k)


# l   r     r
# a b a d e f
#     "abcdeca"
# "bcdeca" "abcdec"
# "cdeca".  "abcdeca"


# Output: True
print(Solution().isValidPalindrome(s="abcdeca", k=2))

# Output: False
print(Solution().isValidPalindrome(s="abcde", k=1))

# Output: True
print(Solution().isValidPalindrome(s="aba", k=0))

# Output: True
print(Solution().isValidPalindrome(s="abca", k=1))
