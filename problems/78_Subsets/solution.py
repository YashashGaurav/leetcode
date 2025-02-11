'''
    78. Subsets
'''
from typing import List

class Solution:

    # backtracking - iteration
    def subsets(self, nums: List[int]) -> List[List[int]]:

        return_sets = [[]]

        for num in nums:
            collection_set = []
            for subset in return_sets:
                temp_set = subset.copy()
                collection_set.append(temp_set.copy())
                temp_set.append(num)
                collection_set.append(temp_set.copy())
            return_sets = collection_set

        return return_sets

    # backtracking - Trees
    def subsets_1(self, nums: List[int]) -> List[List[int]]:
        
        return_sets = []

        def dfs(index, current_subset):

            if index >= len(nums):
                return_sets.append(current_subset.copy())
                return
            
            # left case - adding to subset
            current_subset.append(nums[index])
            dfs(index+1, current_subset)

            # right case - not adding the subset
            current_subset.pop()
            dfs(index+1, current_subset)
        
        dfs(0, [])
        return return_sets
        

    
    def subset_0(self, nums):
        pass
        
        # for subset_len in range(1, len(nums)+1):
        #     for i in range(0, len(nums) - subset_len + 1):
        #         return_sets.append(nums[i:i+subset_len])
        
        # return return_sets


print(Solution().subsets(nums = [1,2,3]))
print(Solution().subsets(nums = [0]))