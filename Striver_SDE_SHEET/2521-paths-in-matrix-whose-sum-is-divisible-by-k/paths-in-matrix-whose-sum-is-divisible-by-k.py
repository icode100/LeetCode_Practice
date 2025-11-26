class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = int(1e9+7)
        R,C = len(grid),len(grid[0])

        dp = [[[0 for _ in range(k)] for __ in range(C+1)] for ___ in range(R+1)]

        for mod in range(k): 
            newmod = (mod+grid[R-1][C-1]%k)%k
            dp[R-1][C-1][mod] = 1 if newmod==0 else 0

        for r in range(R-1,-1,-1):
            for c in range(C-1,-1,-1):
                if r==R-1 and c==C-1: continue 
                for mod in range(k):

                    newmod = (mod+ grid[r][c]%k )%k

                    down = dp[r+1][c][newmod] % MOD if r+1<R else 0
                    right = dp[r][c+1][newmod] % MOD if c+1<C else 0

                    dp[r][c][mod] = (down+right) % MOD

        return dp[0][0][0] % MOD

        # @cache
        # def recursion(r,c,mod):
            
        #     if r==R-1 and c==C-1 and ((mod+(grid[r][c]%k))%k)==0: return 1
        #     if r>=R or c>=C: return 0

        #     down = recursion(r+1,c,(mod+(grid[r][c]%k))%k) % MOD
        #     right = recursion(r,c+1,(mod+(grid[r][c]%k))%k) % MOD

        #     return (down+right) % MOD
        
        # return recursion(0,0,0)