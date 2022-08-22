"""
    342. Power of Four
"""


# Accepted	65 ms	13.9 MB
class Solution1:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        elif n == 1:
            return True
        # binary with one trailed by even number of zeros
        n_bin = bin(n)
        if n_bin[2] == "1":
            return self.test_even_zeros(n_bin[3:])
        else:
            return False

    def test_even_zeros(self, s):
        if s == "00":
            return True
        elif s[0:2] == "00":
            return self.test_even_zeros(s[2:])
        return False


# Accepted	54 ms	13.8 MB
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        a = bin(n)[3:]
        return n > 0 and ("1" not in a) and len(a) % 2 == 0


print(Solution().isPowerOfFour(16))  # true
print(Solution().isPowerOfFour(5))  # false
print(Solution().isPowerOfFour(1))  # true
print(Solution().isPowerOfFour(-2147483648))  # false
print(Solution().isPowerOfFour(-2147483647))  # false
