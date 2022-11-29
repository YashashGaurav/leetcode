'''
    207. Course Schedule
'''
from typing import List
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        req = collections.defaultdict(list)
        
        
        for prereq in prerequisites:
            req[prereq[0]].append(prereq[1])
            
        
        def _can_finish(idx, visited):
            
            if len(req[idx]) == 0:
                return True
            elif idx in visited:
                return False
            
            visited.append(idx)
            
            for course in req[idx]:
                if not _can_finish(course, visited):
                    return False
                    
            req[idx] = []
            return True
            
                
        for i in range(numCourses):
            if not _can_finish(i, []):
                return False
        
        return True
                
            
            
        
        
        
        
        
        
        

        
#
# numCourses = 5
# prerequisites = [
#           [0, 1],
#           [0, 2],
#           [1, 3],
#           [3, 5],
#           [1, 5],
# ]
#
#
# req = {
#   0: [1, 2]
#   1: [3, 5]
#   3: [5]
# }
#
# _can_finish(0):
# visited = [0, ]
# idx = 0
#
# _can_finish(1):
# visited = [0, ]
# idx = 1


# _can_finish(3, []):
# visited = [3, ]
# idx = 3

# _can_finish(5, [3, ]):
# visited = [3, 5]
# idx = 5
#####################
# [[1, 0]]
# numCourses = 2

# req = {1: [0]}

# _can_finish(1, []):
# visited = [1]
# idx = 0

# _can_finish(1, [1]):
# visited = [1]
# idx = 0

