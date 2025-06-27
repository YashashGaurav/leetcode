'''
    295. Find Median from Data Stream
'''

import heapq

# 81.55% | 18.07%
class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []

    def addNum(self, num: int) -> None:
        # add to left
        heapq.heappush(self.left_max_heap, -1 * num)

        # if left's top greater than right top, move
        if self.left_max_heap and self.right_min_heap and self.left_max_heap[0] * -1 > self.right_min_heap[0]:
            temp = heapq.heappop(self.left_max_heap)
            heapq.heappush(self.right_min_heap, temp * -1)

        # if dis-balanced - move
        if len(self.left_max_heap) - len(self.right_min_heap) > 1:
            temp = heapq.heappop(self.left_max_heap)
            heapq.heappush(self.right_min_heap, temp * -1)
        elif len(self.right_min_heap) - len(self.left_max_heap) > 1:
            temp = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap, temp * -1)

    def findMedian(self) -> float:
        # if same size: take average
        if len(self.right_min_heap) == len(self.left_max_heap):
            return ((self.left_max_heap[0] * -1) + self.right_min_heap[0])/2
        # if disbalanced - take the side that is bigger
        elif len(self.left_max_heap) > len(self.right_min_heap):
            return self.left_max_heap[0] * -1
        else:
            return self.right_min_heap[0]
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()