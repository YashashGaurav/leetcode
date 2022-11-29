"""
    70. Climbing Stairs
"""


class Solution:

    def __init__(self):
        self.step_store = {}

    def _count_steps(self, n: int):
        if n < 2:
            return 1
        if n not in self.step_store:
            left = self._count_steps(n - 1)
            right = self._count_steps(n - 2)
            self.step_store[n] = left + right
        return self.step_store[n]

    # Accepted	61 ms	13.9 MB
    def climbStairs0(self, n: int) -> int:
        return self._count_steps(n)

    # Accepted	51 ms	13.9 MB
    def climbStairs(self, n: int) -> int:
        # if n is small
        if n <= 2:
            return n
        
        dp = [0]*n
        
        dp[-1], dp[-2] = 1, 2
        

        for i in range(n-3, -1, -1):
            dp[i] = dp[i+1] + dp[i+2]
        
        return dp[0]
    
# n = 5
# [0, 0, 0, 2, 1]
#.          i   

# n = 3
# [0, 2, 1]
#. i    


print(Solution().climbStairs(16))
print(Solution().climbStairs(5))
print(Solution().climbStairs(1))
print(Solution().climbStairs(45))
