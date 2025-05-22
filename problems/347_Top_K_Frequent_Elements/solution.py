"""
347. Top K Frequent Elements
"""

import heapq
from collections import Counter, defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [key for key, val in Counter(nums).most_common(k)]

    def topKFrequent_0(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(lambda: 0)
        for num in nums:
            counter[num] += 1

        max_heap = []
        for key, value in counter.items():
            heapq.heappush(max_heap, (-value, key))

        return [heapq.heappop(max_heap)[1] for _ in range(k)]


# Output: [1,2]
print(Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))

# Output: [1]
print(Solution().topKFrequent(nums=[1], k=1))

print(Solution().topKFrequent(nums=[1, 2], k=2))
