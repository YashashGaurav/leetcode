'''
    202. Happy Number
'''


# Accepted	38 ms	13.8 MB
class Solution:
    def isHappy(self, n: int) -> bool:
        memory = set()
        while n!= 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in memory:
                return False
            else:
                memory.add(n)
        return True


print(Solution().isHappy(19))
