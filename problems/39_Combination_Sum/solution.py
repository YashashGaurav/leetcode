'''
    39. Combination Sum
'''

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []	

        def dfs(can_pointer, curr_sol, remaining_sum):

            if remaining_sum == 0:
                res.append(curr_sol.copy())
                return
            elif remaining_sum < 0:
                return

            for i in range(can_pointer, len(candidates)):
                curr_sol.append(candidates[i])
                dfs(i, curr_sol, remaining_sum - candidates[i])
                curr_sol.pop()

        dfs(0, [], target)
        
        return res

