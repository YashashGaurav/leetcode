"""
49. Group Anagrams
"""

from collections import defaultdict
from typing import List


class Solution:
    # 19.13% | 12.94
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)
        for string in strs:
            key_val = [0] * 26
            for char in string:
                key_val[ord(char) - ord("a")] += 1
            cache[tuple(key_val)].append(string)
        return list(cache.values())

    # 55.29% || 43.50%
    def groupAnagrams_0(self, strs: List[str]) -> List[List[str]]:
        cache: dict[tuple, List[str]] = defaultdict(list)
        for string in strs:
            str_key = tuple(sorted(string))
            cache[str_key].append(string)

        return [cache[k] for k in cache]


# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# Output: [[""]]
print(Solution().groupAnagrams([""]))

# Output: [["a"]]
print(Solution().groupAnagrams(["a"]))
