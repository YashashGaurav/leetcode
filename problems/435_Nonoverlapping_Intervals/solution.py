'''
    435. Non-overlapping Intervals
'''

from typing import List
import random

class Solution:
    
    def quick_sort_intervals(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        pivot = random.choice(intervals)

        head = self. quick_sort_intervals([x for x in intervals if x[0] < pivot[0]])
        equal = [x for x in intervals if x[0] == pivot[0]]
        tail = self.quick_sort_intervals([x for x in intervals if x[0] > pivot[0]])

        return head + equal + tail

    # Accepted	5837 ms	53.5 MB	
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        intervals = self.quick_sort_intervals(intervals)
        remove_count = 0
        largest_last = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if largest_last > intervals[i][0]:
                if largest_last > intervals[i][1]:
                    largest_last = intervals[i][1]
                remove_count += 1
            else:
                largest_last = intervals[i][1]
                
        return remove_count


print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(Solution().eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))
