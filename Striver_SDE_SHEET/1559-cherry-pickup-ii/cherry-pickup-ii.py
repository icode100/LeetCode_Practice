class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        N,M = len(grid),len(grid[0])
        dp = [[[-1 for _ in range(M)] for _ in range(M)] for _ in range(N)]
        if M == 1:
            dp[0][0][0] = grid[0][0]
        else:
            dp[0][0][M-1] = grid[0][0] + grid[0][M-1]
        for r in range(1, N):
            for c1 in range(M):
                for c2 in range(M):
                    max_prev = -1                    
                    for pc1 in [c1-1, c1, c1+1]: 
                        for pc2 in [c2-1, c2, c2+1]:                            
                            if 0 <= pc1 < M and 0 <= pc2 < M:
                                if dp[r-1][pc1][pc2] != -1:
                                    max_prev = max(max_prev, dp[r-1][pc1][pc2])
                    if max_prev == -1:
                        continue 
                    cherries = 0
                    if c1 == c2:
                        cherries = grid[r][c1]
                    else:
                        cherries = grid[r][c1] + grid[r][c2]
                    dp[r][c1][c2] = max_prev + cherries
        max_cherries = 0
        for c1 in range(M):
            for c2 in range(M):
                max_cherries = max(max_cherries, dp[N-1][c1][c2])
        return max_cherries