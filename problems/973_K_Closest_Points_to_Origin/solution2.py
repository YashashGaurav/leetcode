"""
973. K Closest Points to Origin
"""

import heapq
import math
from typing import List


class Solution:
    def kClosest_0(self, points: List[List[int]], k: int) -> List[List[int]]:
        top_k = []

        for point in points:
            point_dist_origin = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(top_k, (point_dist_origin, point))

        res = []
        for i in range(k):
            _, point = heapq.heappop(top_k)
            res.append(point)

        return res

    # 57.23% | 82.41%
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points = []

        for point in points:
            dist = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(closest_points, (-dist, point))

            if len(closest_points) > k:
                heapq.heappop(closest_points)

        return [data[1] for data in closest_points]
