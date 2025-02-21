"""
167. Two Sum II - Input Array Is Sorted
"""

from typing import List


class Solution:
    # 30.64% | 90.43%
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        ileft, iright = 0, len(numbers) - 1

        while ileft < iright:
            if numbers[ileft] + numbers[iright] == target:
                return [ileft + 1, iright + 1]
            elif numbers[ileft] + numbers[iright] > target:
                iright -= 1
            elif numbers[ileft] + numbers[iright] < target:
                ileft += 1

    # 5.05% | 9.60%
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        # binary search

        def binary_search(ileft, iright, target):
            if ileft > iright:
                return -1

            imed = (ileft + iright) // 2
            if target == numbers[imed]:
                return imed
            elif target > numbers[imed]:
                return binary_search(imed + 1, iright, target)
            elif target < numbers[imed]:
                return binary_search(ileft, imed - 1, target)

        for i in range(len(numbers)):
            num2 = target - numbers[i]
            inum2 = binary_search(i + 1, len(numbers) - 1, num2)
            if inum2 != -1:
                return [i + 1, inum2 + 1]

    # TLE
    def twoSum0(self, numbers: List[int], target: int) -> List[int]:
        # brute force
        for i in range(len(numbers)):
            num2 = target - numbers[i]
            for j in range(i + 1, len(numbers)):
                if num2 == numbers[j]:
                    return [i + 1, j + 1]


# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
print(Solution().twoSum(numbers=[2, 7, 11, 15], target=9))

# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
print(Solution().twoSum(numbers=[2, 3, 4], target=6))

# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
print(Solution().twoSum(numbers=[-1, 0], target=-1))

print(Solution().twoSum(numbers=[5, 25, 75], target=100))
