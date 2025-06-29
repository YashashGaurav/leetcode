"""
691. Stickers to Spell Word
"""

from typing import List


class Solution:
    # 26.57% | 33.49% - Took more than 2 hours to solve ugh
    def minStickers(self, stickers: List[str], target: str) -> int:
        # tokenize
        cache = {}
        sticker_char_counts = []
        for isticker, sticker in enumerate(stickers):
            sticker_char_counts.append({})
            for sticker_char in sticker:
                sticker_char_counts[isticker][sticker_char] = 1 + sticker_char_counts[isticker].get(sticker_char, 0)

        def dfs(target):
            if target in cache:
                return cache[target]

            if target == "":
                return 0

            stickers_used = float("inf")
            for sticker_candidate in sticker_char_counts:
                sticker_candidate_copy = sticker_candidate.copy()
                common_char_count = set(target).intersection(set(sticker_candidate_copy.keys()))
                if len(common_char_count) == 0:
                    continue

                remaining_target = ""

                for tar_char in target:
                    if tar_char in sticker_candidate_copy and sticker_candidate_copy[tar_char] > 0:
                        sticker_candidate_copy[tar_char] -= 1
                    else:
                        remaining_target += tar_char

                if len(remaining_target) < len(target):
                    stickers_used = min(stickers_used, 1 + dfs(remaining_target))

            cache[target] = stickers_used
            return cache[target]

        res = dfs(target)
        # if res is inf then -1
        return -1 if res == float("inf") else res

    # TLE - needs caching
    def minStickers_0(self, stickers: List[str], target: str) -> int:
        # tokenize
        sticker_char_counts = []
        for isticker, sticker in enumerate(stickers):
            sticker_char_counts.append({})
            for sticker_char in sticker:
                sticker_char_counts[isticker][sticker_char] = 1 + sticker_char_counts[isticker].get(sticker_char, 0)

        def dfs(target, sticker_char_count):
            if target == "":
                return 0
            # if no sticker in sticker then mycount = 0, else 1
            # clear any chars you can

            if sticker_char_count:
                my_count = 1
                remaining_target = ""
                for tar_char in target:
                    if tar_char in sticker_char_count and sticker_char_count[tar_char] > 0:
                        sticker_char_count[tar_char] -= 1
                    else:
                        remaining_target += tar_char

            else:
                remaining_target = target
                my_count = 0

            # for any chars that remain, dfs for each sticker
            if remaining_target:
                stickers_used = float("inf")

                # if there are no chars that match then return inf
                for sticker_candidate in sticker_char_counts:
                    if remaining_target[0] in sticker_candidate:
                        stickers_used = min(stickers_used, dfs(remaining_target, sticker_candidate.copy()))

            else:
                return 1

            return my_count + stickers_used

        res = dfs(target, {})
        # if res is inf then -1
        return -1 if res == float("inf") else res


# Output: 3
# print(Solution().minStickers(stickers=["with", "example", "science"], target="thehat"))

# Output: -1
# print(Solution().minStickers(stickers=["notice", "possible"], target="basicbasic"))

# Output: 3
print(Solution().minStickers(stickers=["these", "guess", "about", "garden", "him"], target="atomher"))


# thehat

# (with, example, science)

# ehat

# (with, example, science)

# ht

# (with, example, science)

# null
