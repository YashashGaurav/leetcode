"""
    973. K Closest Points to Origin
"""
from typing import List
import heapq
import math

# Accepted	1371 ms	20.5 MB
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.min_heap = []

        for point in points:
            heapq.heappush(
                self.min_heap, (math.sqrt(point[0] ** 2 + point[1] ** 2), point)
            )

        return_list = []
        for i in range(k):
            _, point = heapq.heappop(self.min_heap)
            return_list.append(point)

        return return_list


print(Solution().kClosest([[1, 3], [-2, 2]], k=1))
print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], k=2))

