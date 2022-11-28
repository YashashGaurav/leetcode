'''
    55. Jump Game
'''

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # last index is already at the last:
        latest_possible = len(nums) - 1
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= latest_possible - i:
                latest_possible = i
        
        
        if nums[0] >= latest_possible:
            return True
        return False
        

print(Solution().canJump([3,2,1,0,4])) # False
