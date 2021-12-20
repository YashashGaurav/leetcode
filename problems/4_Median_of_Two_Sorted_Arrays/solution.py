from typing import List
from math import floor


class Solution0:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        def merger(nums1: List[int], nums2: List[int]) -> List[int]:
            if not nums1 and not nums2:
                return [0]
            elif not nums1:
                return nums2
            elif not nums2:
                return nums1
            else:
                if nums1[0] <= nums2[0]:
                    return [nums1.pop(0)] + merger(nums1, nums2)
                else:
                    return [nums2.pop(0)] + merger(nums1, nums2)

        def median(list: List[int]):
            if len(list) % 2 != 0:
                return list[int(len(list) / 2)]
            else:
                return (
                    list[int(len(list) / 2)] + list[int(len(list) / 2) - 1]
                ) / 2

        merged_list = merger(nums1, nums2)
        return median(merged_list)


class Solution1:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        net_size = len(nums1) + len(nums2)
        avg_index = floor((net_size - 1) / 2)
        aggregate: List[int] = []
        for i in range(0, len(nums1) + len(nums2)):
            if len(aggregate) > avg_index + 1:
                break
            elif not nums1:
                aggregate += nums2
            elif not nums2:
                aggregate += nums1
            else:
                if nums1[0] <= nums2[0]:
                    aggregate += [nums1.pop(0)]
                else:
                    aggregate += [nums2.pop(0)]
        if net_size % 2 == 0:
            return (aggregate[avg_index] + aggregate[avg_index + 1]) / 2
        else:
            return aggregate[avg_index]


## This needs more work, but i'm tired yo
class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        if len(nums1) > len(nums2):
            self.findMedianSortedArrays(nums2, nums1)

        hi1 = len(nums1) - 1
        lo1 = 0
        mid1 = int(len(nums1) / 2)
        while mid1 != 0 or mid1 != (len(nums1) - 1):
            mid1 = hi1 - lo1
            mid2 = len(nums1) + len(nums2) - mid1

            if nums1[mid1] < nums2[mid2 + 1] and nums2[mid2] < nums1[mid1 + 1]:
                if len(nums1) + len(nums2) % 2:
                    return max(nums1[mid1], nums2[mid2])
                else:
                    return (
                        max(nums1[mid1], nums2[mid2])
                        + max(nums1[mid1 + 1], nums2[mid2 + 1])
                    ) / 2
            elif nums1[mid1] > nums2[mid1 + 1]:
                hi1 = mid1
            else:
                lo1 = mid1 + 1


solution = Solution()

# 2
print(solution.findMedianSortedArrays([1, 3], [2]))
# 2.5
print(solution.findMedianSortedArrays([1, 2], [3, 4]))
# 2.5
print(solution.findMedianSortedArrays([1, 3], [2, 7]))
