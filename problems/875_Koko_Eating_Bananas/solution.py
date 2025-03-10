"""
875. Koko Eating Bananas
"""

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        return_speed = right

        while left <= right:
            mid = (left + right) // 2
            current_h = 0

            for i in range(len(piles)):
                current_h += math.ceil(piles[i] / mid)

            if current_h <= h:
                return_speed = mid
                right = mid - 1
            else:
                left = mid + 1

        return return_speed

    # TLE
    def minEatingSpeed_0(self, piles: List[int], h: int) -> int:
        piles.sort(reverse=True)
        current_speed = 1

        while True:
            current_h = 0
            current_speed -= 1

            for i in range(len(piles)):
                if piles[i] > current_speed:
                    current_h += math.ceil(piles[i] / current_speed)
                else:
                    current_h += len(piles[i:])
                    break

            if current_h <= h:
                break

        return current_speed + 1


print(Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8))  # 4
print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))  # 30
print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))  # 23
print(Solution().minEatingSpeed(piles=[312884470], h=312884469))  # 23
