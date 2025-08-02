"""
480. Sliding Window Median
"""

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left_heap = []  # max heap
        right_heap = []  # min heap

        to_delete = defaultdict(lambda: 0)
        res = []

        # helpers:

        def clean_heaps():
            while left_heap and to_delete[-left_heap[0]] > 0:
                removed = heapq.heappop(left_heap)
                to_delete[-removed] -= 1

            while right_heap and to_delete[right_heap[0]] > 0:
                removed = heapq.heappop(right_heap)
                to_delete[removed] -= 1

        def balance_heaps():
            clean_heaps()

            target_left_size = (k + 1) // 2
            target_right_size = k // 2

            while len(left_heap) > target_left_size:
                left_heap_removed = heapq.heappop(left_heap)
                heapq.heappush(right_heap, -left_heap_removed)
                clean_heaps()

            while len(right_heap) > target_right_size:
                right_heap_removed = heapq.heappop(right_heap)
                heapq.heappush(left_heap, -right_heap_removed)
                clean_heaps()

            while len(left_heap) < target_left_size and right_heap:
                val = heapq.heappop(right_heap)
                heapq.heappush(left_heap, -val)
                clean_heaps()

            while len(right_heap) < target_right_size and left_heap:
                val = heapq.heappop(left_heap)
                heapq.heappush(right_heap, -val)
                clean_heaps()

        def add_num(num):
            if not left_heap or num <= -left_heap[0]:
                heapq.heappush(left_heap, -num)
            else:
                heapq.heappush(right_heap, num)

        def get_median():
            clean_heaps()
            if k % 2 == 1:
                return -left_heap[0]
            else:
                return (-left_heap[0] + right_heap[0]) / 2

        for i in range(k):
            add_num(nums[i])
            balance_heaps()

        res.append(get_median())

        for i in range(k, len(nums)):
            to_delete[nums[i - k]] += 1
            add_num(nums[i])

            balance_heaps()

            res.append(get_median())

        return res


# Expected Output: [1 ,-1 ,-1 ,3 ,5 ,6 ]
# Execution output: [1, -1, -1, 3, 3, 3]
# print(Solution().medianSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))

# Expected Output: [2 ,3 ,3 ,3 ,2 ,3 ,2 ]
# Execution output: [2, 2, 2, 2, 2, 3, 2]
# print(Solution().medianSlidingWindow(nums=[1, 2, 3, 4, 2, 3, 1, 4, 2], k=3))


print(Solution().medianSlidingWindow(nums=[2147483647, 1, 2, 3, 4, 5, 6, 7, 2147483647], k=2))
