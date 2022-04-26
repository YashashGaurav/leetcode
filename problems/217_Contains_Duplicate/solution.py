from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = set()

        for i in range(len(nums)):
            if nums[i] in cache:
                return "true"
            else:
                cache.add(nums[i])
        return "false"


print(Solution().containsDuplicate([1, 2, 3, 1]))
print(Solution().containsDuplicate([1, 2, 3, 4]))
print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
