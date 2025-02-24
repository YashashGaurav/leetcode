"""
15. 3Sum
"""

from typing import List


class Solution:
    # 32.20% | 69.24%
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # with sorting

        resulting_triplets = []
        # nums = sorted(list(set(nums)))
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            # if nums[i] is positive and all the values are positive they will never sum to 0
            if nums[i] > 0:
                break

            ileft, iright = i + 1, len(nums) - 1

            while ileft < iright:
                if nums[i] + nums[ileft] + nums[iright] > 0:
                    iright -= 1
                    while nums[iright] == nums[iright + 1]:
                        iright -= 1
                elif nums[i] + nums[ileft] + nums[iright] < 0:
                    ileft += 1
                    while nums[ileft] == nums[ileft - 1] and ileft < iright:
                        ileft += 1
                else:
                    resulting_triplets.append([nums[i], nums[ileft], nums[iright]])
                    ileft += 1
                    while nums[ileft] == nums[ileft - 1] and ileft < iright:
                        ileft += 1

        return resulting_triplets

    # TLE
    def threeSum0(self, nums: List[int]) -> List[List[int]]:
        return_triplets = set()
        cache = {}

        for i in range(len(nums)):
            if nums[i] in cache:
                cache[nums[i]].append(i)
            else:
                cache[nums[i]] = [i]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                target = 0 - nums[i] - nums[j]
                if target in cache:
                    for k in cache[target]:
                        if i != k and j != k:
                            sub_set = sorted([nums[i], nums[j], nums[k]])
                            sub_set_str = ""
                            for num in sub_set:
                                sub_set_str += f"{num},"
                            sub_set_str = sub_set_str[:-1]
                            return_triplets.add(sub_set_str)

        return [[int(j) for j in i.split(",")] for i in return_triplets]


print(Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum(nums=[0, 1, 1]))
print(Solution().threeSum(nums=[0, 0, 0]))
print(Solution().threeSum(nums=[0, 0, 0, 0]))
