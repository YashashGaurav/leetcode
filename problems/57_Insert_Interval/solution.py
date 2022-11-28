'''
    57. Insert Interval
'''

from typing import List


class Solution:
    
    def is_overlap(self, interval_1, interval_2):
        if max(interval_1[0], interval_2[0]) <= min(interval_1[1], interval_2[1]):
            return True
        return False
    
    #	Accepted	212 ms	17.5 MB
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        
        results = []
        
        for i in range(len(intervals)):
            
            # when interval is after new interval - enough to return 
            if new_interval[1] < intervals[i][0]:
                results.append(new_interval)
                results += intervals[i:]
                return results
            
            # when new interval is before interval - just add
            elif intervals[i][1] < new_interval[0]:
                results.append(intervals[i])
            
            # when new interval overlaps, combine and keep
            elif self.is_overlap(intervals[i], new_interval):
                new_interval = [min(intervals[i][0], new_interval[0]), max(intervals[i][1], new_interval[1])]
                
        results.append(new_interval)
        
        return results