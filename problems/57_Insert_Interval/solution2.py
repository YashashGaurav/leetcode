"""
57. Insert Interval
"""

from typing import List


class Solution:
    # 2ms - 19.80mb
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        return_intervals = []

        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            return_intervals.append(intervals[i])
            i += 1

        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1]),
            ]
            i += 1
        return_intervals.append(newInterval)

        while i < n:
            return_intervals.append(intervals[i])
            i += 1

        return return_intervals

    def insert_pure_neetcode(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        return_intervals = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                return_intervals.append(newInterval)
                return return_intervals + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                return_intervals.append(intervals[i])

            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]

        return_intervals.append(newInterval)

        return return_intervals


# Output: [[1,5],[6,9]]
print(Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
# [[1,2],[3,10],[12,16]]
print(Solution().insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))


# print(Solution().insert(intervals=[[1, 5]], newInterval=[0, 1]))
# print(Solution().insert(intervals=[[1, 5]], newInterval=[2, 3]))
# print(Solution().insert(intervals=[[1, 5]], newInterval=[5, 6]))
# print(Solution().insert(intervals=[[1, 5]], newInterval=[0, 6]))
