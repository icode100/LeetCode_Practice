class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        zero = [[i,j] for i in range(m) for j in range(n) if grid[i][j]==0]
        extra = [[i,j,grid[i][j]-1] for i in range(m) for j in range(n) if grid[i][j]>1]
        compute_manhattan = lambda x,y: abs(x[0]-y[0])+abs(x[1]-y[1])
        ans = sys.maxsize
        def dfs(i,count):
            nonlocal ans
            if i==len(zero): 
                ans = min(ans,count)
                return
            for j in range(len(extra)):
                if extra[j][2]>0:
                    extra[j][2]-=1
                    dfs(i+1,count+compute_manhattan(extra[j],zero[i]))
                    extra[j][2]+=1
        dfs(0,0)
        return ans
