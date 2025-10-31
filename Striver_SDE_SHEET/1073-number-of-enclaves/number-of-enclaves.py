class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        N,M = len(grid),len(grid[0])
        total = sum([grid[i].count(1) for i in range(len(grid))])
        vis = set()
        def dfs(r,c):
            vis.add((r,c))
            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=nr<N and 0<=nc<M and (nr,nc) not in vis and grid[nr][nc] == 1:
                    dfs(nr,nc)
        for i in range(N):
            if grid[i][0]==1 and (i,0) not in vis: dfs(i,0)
            if grid[i][M-1]==1 and (i,M-1) not in vis: dfs(i,M-1)
        for i in range(M):
            if grid[0][i]==1 and(0,i) not in vis: dfs(0,i)
            if grid[N-1][i]==1 and(N-1,i) not in vis: dfs(N-1,i)
        return total-len(vis)