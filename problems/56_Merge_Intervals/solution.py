'''
    56. Merge Intervals
'''

import random
from typing import List

class Solution:
    
    def quick_sort_intervals(self, intervals):
        if not intervals:
            return intervals
        
        pivot = intervals[random.choice(range(0, len(intervals)))]
        
        head  = self.quick_sort_intervals([x for x in intervals if x[0] < pivot[0]])
        equal = [x for x in intervals if x[0] == pivot[0]]
        tail  = self.quick_sort_intervals([x for x in intervals if x[0] > pivot[0]])
        
        return head + equal + tail
        
    # Accepted	628 ms	18.4 MB	
    def merge0(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = self.quick_sort_intervals(intervals)
        
        res = [intervals[0]]
        
        for interval in intervals[1:]:
            if max(res[-1][0], interval[0]) <= min(res[-1][1], interval[0]):
                res[-1] = [min(res[-1][0], interval[0]), max(res[-1][1], interval[1])]
            else:
                res.append(interval)
            
        return res

    # Accepted	158 ms	18 MB
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key=lambda x: x[0])
        
        res = [intervals[0]]
        
        for interval in intervals[1:]:
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
            
        return res