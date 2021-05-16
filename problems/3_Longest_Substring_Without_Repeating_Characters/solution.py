class Solution0:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        max_length = 0
        last_match_index = 0
        for index, character in enumerate(s):
            if character in char_dict:
                max_length = max(max_length, index - last_match_index)
                last_match_index = index
                char_dict = {}
            elif index == len(s) - 1:
                max_length = max(max_length, index - last_match_index + 1)
            char_dict[character] = index

        if max_length == 0 and len(s) > 0:
            return len(s)
        else:
            return max_length


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for outer_index in range(0, len(s)):
            char_dict = {}
            for inner_index in range(outer_index, len(s)):
                if s[inner_index] in char_dict:
                    max_length = max(max_length, inner_index - outer_index)
                    break
                elif inner_index == len(s) - 1:
                    max_length = max(max_length, inner_index - outer_index + 1)
                else:
                    char_dict[s[inner_index]] = inner_index

        if max_length == 0 and len(s) > 0:
            return len(s)
        else:
            return max_length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_dict = {}
        substr_left_index = 0
        for index, char in enumerate(s):
            if char in char_dict:
                substr_left_index = max(char_dict[char] + 1, substr_left_index)
            char_dict[char] = index
            max_length = max(max_length, index - substr_left_index + 1)

        return max_length


solution = Solution()

# 3
print(solution.lengthOfLongestSubstring("abcabcbb"))
# 2
print(solution.lengthOfLongestSubstring("aab"))
# 1
print(solution.lengthOfLongestSubstring(" "))
# 0
print(solution.lengthOfLongestSubstring(""))
# 2
print(solution.lengthOfLongestSubstring("au"))
# 3
print(solution.lengthOfLongestSubstring("pwwkew"))
# 2
print(solution.lengthOfLongestSubstring("cdd"))
# 3
print(solution.lengthOfLongestSubstring("dvdf"))
# 2
print(solution.lengthOfLongestSubstring("abba"))
