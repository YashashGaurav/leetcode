'''
    261. Graph Valid Tree
'''

import collections
from typing import List


class Solution:
    # Accepted	191 ms	16.1 MB
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adjSet = collections.defaultdict(list)
        
        if len(edges) != n-1:
            return False
        
        adjSet = {i: [] for i in range(n)}
        
        for n1, n2 in edges:
            adjSet[n1].append(n2)
            adjSet[n2].append(n1)
            
            
        visited = set()
        
        def dfs(i, prev):
            
            if i in visited:
                return False
            
            visited.add(i)
            
            for j in adjSet[i]:
                if j == prev:
                    continue
                
                if not dfs(j, i):
                    return False
                    
            return True
        
        return dfs(0, -1) and len(visited) == n
        
        
        
# not good enough:
# conditions of a vaild Tree:
# Edges: n-1
# every node has atleast one edge