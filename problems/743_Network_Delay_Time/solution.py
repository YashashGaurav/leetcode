"""
    743. Network Delay Time
"""

import heapq
import collections
from typing import List


class Solution:
    # Accepted	1320 ms	16.1 MB
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, t in times:
            if u in edges:
                edges[u].append((v, t))
            else:
                edges[u] = [(v, t)]

        minHeap = []
        heapq.heappush(minHeap, (0, k))

        visited = set()
        max_t = 0

        while minHeap:
            t1, v1 = heapq.heappop(minHeap)

            if v1 in visited:
                continue

            max_t = max(t1, max_t)

            visited.add(v1)

            for v2, t2 in edges[v1]:
                if v2 not in visited:  # optimizing heappush and heappops
                    heapq.heappush(minHeap, (t1 + t2, v2))

        return max_t if len(visited) == n else -1


# print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
# print(Solution().networkDelayTime([[1, 2, 1]], 2, 2))
print(Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,1]], 3, 2))
