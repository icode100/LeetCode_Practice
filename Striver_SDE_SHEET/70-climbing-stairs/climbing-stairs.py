class Solution:
    def climbStairs(self, n: int) -> int:
        # dp = [0]*(n+2)
        dp_n = 1
        dp_n_1 = 0
        dp = 0
        for i in range(n-1,-1,-1):
            dp = dp_n+dp_n_1
            dp_n_1 = dp_n
            dp_n = dp
        return dp