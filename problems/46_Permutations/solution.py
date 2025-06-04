"""
46. Permutations
"""

from typing import List


class Solution:
    # Beats 100.00% | Beats 81.44%
    def permute(self, nums: List[int]) -> List[List[int]]:
        def find_permutation(numbers, collection):
            if len(numbers) == 0:
                return [[]]

            perms = find_permutation(numbers[1:], [])

            for perm in perms:
                for j in range(len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(j, numbers[0])
                    collection.append(perm_copy)

            return collection

        res = find_permutation(nums, [])
        return res


# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(Solution().permute(nums=[1, 2, 3]))


# Output: [[0,1],[1,0]]
print(Solution().permute(nums=[0, 1]))


# Output: [[1]]
print(Solution().permute(nums=[1]))
