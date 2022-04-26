from typing import List


class Solution:
    def threeSum0(self, nums: List[int]) -> List[List[int]]:
        sorted_input = sorted(set(nums))
        start = 0
        end = len(sorted_input) - 1

        return_list = []

        while start < end:
            if -(sorted_input[start] + sorted_input[end]) in sorted_input:
                return_list.append([sorted_input[start], -(sorted_input[start] + sorted_input[end]), sorted_input[end]])
            if sorted_input[start] + sorted_input[end] < sorted_input[int((end - start)/2)]:
                start += 1
            else:
                end -= 1
                
        return return_list

    # brute force
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        return_set = set()
        for pivot_index in range(len(nums)):
            num1 = nums.pop(pivot_index)
            for j in range(len(nums)):
                num2 = nums.pop(j)
                if -(num1 + num2) in nums:
                    return_set.add(tuple(sorted([num1, num2, -(num1 + num2)])))
                nums.insert(j, num2)
            nums.insert(pivot_index, num1)

        return list(list(i) for i in return_set)

    # 3 sum as a two pointer problem.
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # following will work only on a sorted array
        result = []

        # left index is our pivot of sorts.
        for left in range(len(nums) - 2):
            # if we have seen the same number last time, we have calculated the
            # unique solutions possible
            if left > 0 and nums[left] == nums[left-1]:
                continue

            middle, right = left + 1, len(nums) - 1
            while middle < right:
                sum = nums[left] + nums[middle] + nums[right]
                if sum < 0:
                    middle += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[left], nums[middle], nums[right]])
                    # skip numbers if you have seen them before.
                    while middle < right and nums[middle] == nums[middle+1]:
                        middle += 1
                    while middle < right and nums[right] == nums[right-1]:
                        right -= 1
                    middle += 1
                    right -= 1
        return result    

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ref_table = {}
        for index, val in enumerate(nums):
            if val in ref_table:
                ref_table[val].add(index)
            else:
                ref_table[val] = [index]
        
        for pivot_val, pivot_indexes in ref_table.values():
            if len(pivot_indexes) > 1:
                for i in 


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))

