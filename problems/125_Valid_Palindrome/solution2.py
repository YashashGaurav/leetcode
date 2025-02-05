"""
125. Valid Palindrome
"""


class Solution:
    # 7ms 81.10% - Feb 04, 2025 23:06
    def isPalindrome(self, s: str) -> bool:
        left_ptr = 0
        right_ptr = len(s) - 1

        while left_ptr < right_ptr:
            while not str(s[left_ptr]).isalnum() and left_ptr < right_ptr:
                left_ptr += 1
            while not str(s[right_ptr]).isalnum() and right_ptr > left_ptr:
                right_ptr -= 1

            if s[left_ptr].lower() != s[right_ptr].lower():
                return False

            left_ptr += 1
            right_ptr -= 1

        return True


sol = Solution()

print(sol.isPalindrome("A man, a plan, a canal: Panama"))

print(sol.isPalindrome("race a car"))

print(sol.isPalindrome(" "))

print(sol.isPalindrome(".,"))
