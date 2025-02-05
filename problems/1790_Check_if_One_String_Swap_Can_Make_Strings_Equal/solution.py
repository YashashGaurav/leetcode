"""
1790. Check if One String Swap Can Make Strings Equal
"""


class Solution:
    # 0ms 100%
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # make sure number of each alphabet in each string is the same
        s1_dict, s2_dict = {}, {}
        for i in range(len(s1)):
            if s1[i] in s1_dict:
                s1_dict[s1[i]] += 1
            else:
                s1_dict[s1[i]] = 1

            if s2[i] in s2_dict:
                s2_dict[s2[i]] += 1
            else:
                s2_dict[s2[i]] = 1

        if s2_dict != s1_dict:
            return False

        # find the indices that are swappable
        swap_size = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swap_size += 1
                if swap_size > 2:
                    return False

        return True


sol = Solution()

print(sol.areAlmostEqual(s1="bank", s2="kanb"))

print(sol.areAlmostEqual(s1="attack", s2="defend"))

print(sol.areAlmostEqual(s1="kelb", s2="kelb"))
