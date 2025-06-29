"""
680. Valid Palindrome II
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        start_ptr, end_ptr = 0, len(s) - 1

        while start_ptr <= end_ptr:
            if s[start_ptr] != s[end_ptr]:
                # delete start_ptr
                if self.is_palindrome(s[start_ptr + 1 : end_ptr + 1]):
                    return True
                # delete end_ptr
                if self.is_palindrome(s[start_ptr:end_ptr]):
                    return True
                return False

            start_ptr += 1
            end_ptr -= 1

        return True

    def is_palindrome(self, s):
        start_ptr, end_ptr = 0, len(s) - 1

        while start_ptr < end_ptr:
            if s[start_ptr] != s[end_ptr]:
                return False

            start_ptr += 1
            end_ptr -= 1

        return True
