"""
295. Find Median from Data Stream
"""

import heapq


# 137 ms Beats 62.85% | Memory 40.73 MB Beats 5.87%
class MedianFinder:
    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_heap, -num)

        # make sure everything in left_heap in smaller than right_heap
        if self.left_heap and self.right_heap and -self.left_heap[0] > self.right_heap[0]:
            temp = heapq.heappop(self.left_heap)
            heapq.heappush(self.right_heap, -temp)

        # make sure size of the two heaps are same.
        if len(self.left_heap) > len(self.right_heap) + 1:
            temp = heapq.heappop(self.left_heap)
            heapq.heappush(self.right_heap, -temp)
        elif len(self.right_heap) > len(self.left_heap):
            temp = heapq.heappop(self.right_heap)
            heapq.heappush(self.left_heap, -temp)

    def findMedian(self) -> float:
        if len(self.left_heap) == len(self.right_heap):
            return (-self.left_heap[0] + self.right_heap[0]) / 2
        else:
            return -self.left_heap[0]


# TLE
class MedianFinder0:
    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)
        self.data.sort()

    def findMedian(self) -> float:
        mid = (len(self.data) // 2) - 1
        if len(self.data) % 2 == 1:  # odd case
            return self.data[mid + 1]
        else:
            return (self.data[mid] + self.data[mid + 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# Your MedianFinder object will be instantiated and called as such:
medianFinder = MedianFinder()
medianFinder.addNum(1)  # arr = [1]
medianFinder.addNum(2)  # arr = [1, 2]
print(medianFinder.findMedian())  # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)  # arr[1, 2, 3]
print(medianFinder.findMedian())  # return 2.0
