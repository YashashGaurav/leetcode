class Solution:
    @staticmethod
    def is_palindrome(s, start, end):
        if start >= end:
            return True

        if (s[start] == s[end]) and Solution.is_palindrome(
            s, start + 1, end - 1
        ):
            return True
        else:
            return False


test_string = "tattarrattat"

print(Solution().is_palindrome(test_string, 0, len(test_string) - 1))
