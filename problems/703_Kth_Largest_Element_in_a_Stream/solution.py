"""
703. Kth Largest Element in a Stream
"""

import heapq
from typing import List


class KthLargest:
    # 16 ms Beats 62.22%
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)

    def prune_heap(self):
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        self.prune_heap()
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


func = ["KthLargest", "add", "add", "add", "add", "add"]
params = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

for work in zip(func, params):
    obj = {}
    if work[0] == "KthLargest":
        obj = KthLargest(work[1][0], work[1][1])
        print(None)
    elif work[0] == "add":
        print(obj.add(work[1]))
