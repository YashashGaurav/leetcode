'''
    215. Kth Largest Element in an Array
'''

from typing import List
import random

class Solution:
	# 	Accepted	481 ms	27.1 MB	 
    def findKthLargest0(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

    # 	Accepted	546 ms	27.7 MB
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)

        greater_than_pivot = [n for n in nums if n > pivot]
        equal_to_pivot = [n for n in nums if n == pivot]
        less_than_pivot = [n for n in nums if n < pivot]

        g_len = len(greater_than_pivot)
        e_len = len(equal_to_pivot)

        if k <= g_len:
            return self.findKthLargest(greater_than_pivot, k)
        elif k > g_len + e_len:
            return self.findKthLargest(less_than_pivot, k - (g_len + e_len))
        else:
            return equal_to_pivot[0]


print(Solution().findKthLargest([3,2,1,5,6,4], 2))