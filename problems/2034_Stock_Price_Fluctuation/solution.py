'''
    2034. Stock Price Fluctuation
'''
import heapq


# Accepted	2163 ms	61.8 MB
class StockPrice:

    def __init__(self):
        self.book = {}
        self.latest_time = 0
        self.max_heap = []
        self.min_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.book[timestamp] = price

        if timestamp > self.latest_time:
            self.latest_time = timestamp
        
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))


    def current(self) -> int:
        return self.book[self.latest_time]

    def maximum(self) -> int:
        price, timestamp = self.max_heap[0]

        while -price != self.book[timestamp]:
            heapq.heappop(self.max_heap)
            price, timestamp = self.max_heap[0]
        
        return -price


    def minimum(self) -> int:
        price, timestamp = self.min_heap[0]

        while price != self.book[timestamp]:
            heapq.heappop(self.min_heap)
            price, timestamp = self.min_heap[0]
        
        return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp, price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()