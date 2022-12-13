'''
    286. Walls and Gates
'''

from typing import List
from collections import deque

class Solution:
    # Accepted	663  ms	20.6 MB
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        visited = set()
        q = deque()

        def is_out_of_bounds(i, j):
            if (j < 0 or 
                i < 0 or 
                i > ROWS - 1 or 
                j > COLS - 1):
                return True
            
            return False

        def add_room(i, j):
            if ((i, j) in visited or
                is_out_of_bounds(i, j) or
                rooms[i][j] == -1):
                return
            q.append((i, j))
            visited.add((i, j))

        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))

        dist = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                rooms[i][j] = dist
                add_room(i + 1, j)
                add_room(i - 1, j)
                add_room(i, j + 1)
                add_room(i, j - 1)

            dist += 1
