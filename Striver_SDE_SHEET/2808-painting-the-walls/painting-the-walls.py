class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        weight = [t+1 for t in time]
        value = cost
        N = C = len(time)  
        dp = [[0 for _ in range(C+1)] for _ in range(N+1)]
        for i in range(C+1): dp[N][i] = int(1e9)
        for i in range(N+1): dp[i][0] = 0
        for i in range(N-1,-1,-1):
            for c in range(1,C+1):
                dp[i][c] = min(value[i]+dp[i+1][c-weight[i]] if weight[i]<=c else value[i], dp[i+1][c])
        return dp[0][C]
