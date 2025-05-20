"""
56. Merge Intervals
"""

from typing import List


class Solution:
    # 85.6% | 97.5%
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        LEFT = 0
        RIGHT = 1

        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            most_right = res[-1][RIGHT]

            if most_right >= intervals[i][LEFT]:
                # merging
                res[-1][RIGHT] = max(most_right, intervals[i][RIGHT])
            else:
                res.append(intervals[i])

        return res


# [  ]
#      [  ]

# [     ]
#     [    ]

# [        ]
#    [  ]

#   [   ]
# [       ]

#  [    ]
# [  ]

#      [   ]
# [  ]


# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
print(Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))


# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
print(Solution().merge(intervals=[[1, 4], [4, 5]]))
