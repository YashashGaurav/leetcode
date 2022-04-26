class Solution:
    def isPalindrome0(self, input: str) -> bool:
        start = 0
        end = len(input) - 1

        while start < end:
            if not input[start].isalnum():
                start += 1
                continue
            if not input[end].isalnum():
                end -= 1
                continue

            if input[start].lower() != input[end].lower():
                return False

            start += 1
            end -= 1

        return True

    def isPalindrome1(self, input: str) -> bool:
        pal = ""
        for s in input:
            if s.isalnum():
                pal += s.lower()

        return pal == pal[::-1]

    def isPalindrome(self, input: str) -> bool:
        pal = ""
        for s in input:
            if s.isalnum():
                pal += s.lower()

        return pal == ''.join(reversed(pal))


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome(" "))
