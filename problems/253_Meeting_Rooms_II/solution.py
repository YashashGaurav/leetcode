"""
    253. Meeting Rooms II
"""

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        start = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])

        max_meets, current_meets = 0, 0
        sp, ep = 0, 0

        while sp < len(start):
            if start[sp] < end[ep]:
                sp += 1
                current_meets += 1
            else:
                ep += 1
                current_meets -= 1
            max_meets = max(max_meets, current_meets)

        return max_meets

print(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]))  # 2

